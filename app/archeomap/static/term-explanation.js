(function () {
    "use strict";

    tinymce.PluginManager.add("term_explanation", function (editor) {
        const selector = "span[data-term-id]";

        function currentTerm() {
            return editor.dom.getParent(
                editor.selection.getNode(),
                selector
            );
        }

        function openPicker() {
            const existing = currentTerm();
            const range = editor.selection.getRng();

            if (!existing) {
                if (range.collapsed) {
                    editor.windowManager.alert(
                        "Сначала выделите слово или фразу."
                    );
                    return;
                }

                const startBlock = editor.dom.getParent(
                    range.startContainer,
                    editor.dom.isBlock
                );
                const endBlock = editor.dom.getParent(
                    range.endContainer,
                    editor.dom.isBlock
                );

                const fragment = range.cloneContents();

                if (
                    startBlock !== endBlock ||
                    fragment.querySelector(
                        "a, img, span[data-term-id], p, div, ul, ol, table"
                    ) ||
                    editor.dom.getParent(range.startContainer, "a") ||
                    editor.dom.getParent(range.endContainer, "a") ||
                    editor.dom.getParent(range.endContainer, selector)
                ) {
                    editor.windowManager.alert(
                        "Выделите фразу внутри одного абзаца, " +
                        "без ссылок, изображений и других пояснений."
                    );
                    return;
                }
            }

            const text = existing
                ? existing.textContent
                : editor.selection.getContent({ format: "text" });

            if (!text.trim()) {
                editor.windowManager.alert("Выделите текст.");
                return;
            }

            const selectedHtml = existing
                ? existing.innerHTML
                : editor.selection.getContent({ format: "html" });

            const bookmark = editor.selection.getBookmark(2, true);
            let searchOpen = true;

            editor.windowManager.open({
                title: "Найти термин для пояснения",
                body: {
                    type: "panel",
                    items: [
                        {
                            type: "input",
                            name: "query",
                            label: "Название термина",
                        },
                    ],
                },
                initialData: { query: text.trim() },
                buttons: [
                    { type: "cancel", text: "Отмена" },
                    {
                        type: "submit",
                        text: "Найти",
                        primary: true,
                    },
                ],
                onClose: function () {
                    searchOpen = false;
                },
                onSubmit: async function (api) {
                    const query = api.getData().query.trim();

                    if (!query) {
                        editor.windowManager.alert(
                            "Введите название или часть названия."
                        );
                        return;
                    }

                    api.block("Поиск терминов…");

                    try {
                        const endpoint = editor.getElement().getAttribute(
                            "data-glossary-url"
                        );

                        if (!endpoint) {
                            throw new Error("Не настроен адрес API словаря.");
                        }

                        const url = new URL(endpoint, window.location.origin);
                        url.searchParams.set("search", query);

                        const response = await fetch(url, {
                            headers: { Accept: "application/json" },
                            credentials: "same-origin",
                        });

                        if (!response.ok) {
                            throw new Error("Ошибка API: " + response.status);
                        }

                        const data = await response.json();

                        if (!searchOpen) return;

                        api.unblock();

                        if (!Array.isArray(data.results)) {
                            throw new Error("Неожиданный формат ответа API.");
                        }

                        if (!data.results.length) {
                            editor.windowManager.alert(
                                "Термины не найдены. Попробуйте другую " +
                                "формулировку и проверьте публикацию термина."
                            );
                            return;
                        }

                        const terms = data.results;
                        api.close();

                        editor.windowManager.open({
                            title: "Выбрать пояснение",
                            body: {
                                type: "panel",
                                items: [
                                    {
                                        type: "selectbox",
                                        name: "termId",
                                        label: data.next
                                            ? "Первые 20 результатов. Для уточнения повторите поиск."
                                            : "Термин словаря",
                                        items: terms.map(function (term) {
                                            return {
                                                text: term.title,
                                                value: String(term.id),
                                            };
                                        }),
                                    },
                                ],
                            },
                            initialData: {
                                termId: String(terms[0].id),
                            },
                            buttons: [
                                { type: "cancel", text: "Отмена" },
                                {
                                    type: "submit",
                                    text: "Привязать",
                                    primary: true,
                                },
                            ],
                            onSubmit: function (dialog) {
                                const term = terms.find(function (item) {
                                    return String(item.id) ===
                                        dialog.getData().termId;
                                });

                                if (!term) return;

                                dialog.close();
                                editor.focus();

                                editor.undoManager.transact(function () {
                                    if (existing) {
                                        editor.dom.setAttrib(
                                            existing,
                                            "data-term-id",
                                            String(term.id)
                                        );
                                    } else {
                                        editor.selection.moveToBookmark(
                                            bookmark
                                        );

                                        const html = editor.dom.createHTML(
                                            "span",
                                            {
                                                "data-term-id": String(term.id),
                                                class: "term-explanation",
                                            },
                                            selectedHtml
                                        );

                                        editor.insertContent(html);
                                    }
                                });

                                editor.nodeChanged();
                                editor.setDirty(true);
                            },
                        });
                    } catch (error) {
                        if (!searchOpen) return;

                        api.unblock();
                        editor.windowManager.alert(
                            "Не удалось загрузить словарь. " + error.message
                        );
                    }
                },
            });
        }

        editor.ui.registry.addButton("term_explanation", {
            text: "Пояснение",
            tooltip: "Привязать фразу к термину словаря",
            onAction: openPicker,
        });

        editor.ui.registry.addButton("term_explanation_remove", {
            text: "Убрать пояснение",
            tooltip: "Поставьте курсор внутри отмеченной фразы",
            onAction: function () {
                const term = currentTerm();

                if (!term) {
                    editor.windowManager.alert(
                        "Поставьте курсор внутри фразы с пояснением."
                    );
                    return;
                }

                editor.undoManager.transact(function () {
                    editor.dom.remove(term, true);
                });

                editor.nodeChanged();
                editor.setDirty(true);
            },
        });

        editor.on("init", function () {
            editor.dom.addStyle(
                "span[data-term-id] {" +
                "text-decoration: underline dotted;" +
                "text-underline-offset: 3px;" +
                "background-color: #f3ead6;" +
                "}"
            );
        });
    });
})();