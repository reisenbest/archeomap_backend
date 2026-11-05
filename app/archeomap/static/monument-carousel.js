(function () {
    "use strict";

    tinymce.PluginManager.add("monument_carousel", function (editor) {
        const selector = "div.monument-carousel";

        // Экранируем подписи и адреса перед вставкой в HTML.
        function escapeHtml(value) {
            return String(value).replace(/[&<>"']/g, function (char) {
                return {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;",
                }[char];
            });
        }

        function getImages() {
            const raw = editor.getElement().getAttribute(
                "data-carousel-images"
            );

            return JSON.parse(raw || "[]");
        }

        function findCarousel(node) {
            return editor.dom.getParent(node, selector);
        }

        function makeCarousel(images) {
            const ids = images.map(function (image) {
                return image.id;
            }).join(",");

            const slides = images.map(function (image) {
                return (
                    "<figure>" +
                    '<img src="' + escapeHtml(image.url) + '" ' +
                    'alt="' + escapeHtml(image.caption) + '">' +
                    "<figcaption>" +
                    escapeHtml(image.caption) +
                    "</figcaption>" +
                    "</figure>"
                );
            }).join("");

            return (
                '<div class="monument-carousel" ' +
                'contenteditable="false" ' +
                'data-carousel-version="1" ' +
                'data-carousel-ids="' + escapeHtml(ids) + '">' +
                slides +
                "</div>"
            );
        }

        function openDialog(existingBlock) {
            const images = getImages();

            if (images.length < 2) {
                editor.windowManager.alert(
                    "Для карусели нужны минимум две фотографии. " +
                    "Сохраните их в разделе изображений этого памятника " +
                    "и обновите страницу."
                );
                return;
            }

            const oldIds = existingBlock
                ? (existingBlock.getAttribute("data-carousel-ids") || "")
                    .split(",").filter(Boolean)
                : [];

            // Не заменяем незаметно карусель, если исходное фото удалили.
            const availableIds = new Set(images.map(image => image.id));

            if (oldIds.some(id => !availableIds.has(id))) {
                editor.windowManager.alert(
                    "Некоторые фотографии этой карусели больше недоступны. " +
                    "Восстановите их или удалите старый блок и создайте новый."
                );
                return;
            }

            const bookmark = editor.selection.getBookmark(2, true);
            const initialData = {};
            const items = [{
                type: "htmlpanel",
                html: (
                    "<p>Укажите порядок выбранных фотографий: " +
                    "1, 2, 3… Пустое поле — не включать в карусель.</p>"
                ),
            }];

            images.forEach(function (image) {
                const name = "image_" + image.id;
                const index = oldIds.indexOf(image.id);

                initialData[name] = index >= 0
                    ? String(index + 1)
                    : "";

                items.push({
                    type: "htmlpanel",
                    html: (
                        '<img src="' + escapeHtml(image.url) + '" ' +
                        'alt="" style="max-width:180px;max-height:110px;">'
                    ),
                });

                items.push({
                    type: "input",
                    name: name,
                    label: (
                        image.caption || "Фотография № " + image.id
                    ) + " — номер в карусели",
                });
            });

            editor.windowManager.open({
                title: existingBlock
                    ? "Изменить карусель"
                    : "Вставить карусель",
                size: "medium",
                body: {
                    type: "panel",
                    items: items,
                },
                initialData: initialData,
                buttons: [
                    {
                        type: "cancel",
                        text: "Отмена",
                    },
                    {
                        type: "submit",
                        text: "Сохранить карусель",
                        primary: true,
                    },
                ],
                onSubmit: function (api) {
                    const data = api.getData();
                    const selected = [];
                    const usedPositions = new Set();

                    for (const image of images) {
                        const value = (
                            data["image_" + image.id] || ""
                        ).trim();

                        if (!value) {
                            continue;
                        }

                        const position = Number(value);

                        if (
                            !/^[1-9]\d*$/.test(value) ||
                            !Number.isSafeInteger(position) ||
                            usedPositions.has(position)
                        ) {
                            editor.windowManager.alert(
                                "Используйте разные целые положительные " +
                                "номера: 1, 2, 3…"
                            );
                            return;
                        }

                        usedPositions.add(position);
                        selected.push({ image, position });
                    }

                    if (selected.length < 2) {
                        editor.windowManager.alert(
                            "Выберите минимум две фотографии."
                        );
                        return;
                    }

                    selected.sort((a, b) => a.position - b.position);

                    const html = makeCarousel(
                        selected.map(item => item.image)
                    );

                    api.close();
                    editor.focus();

                    editor.undoManager.transact(function () {
                        if (existingBlock) {
                            editor.dom.setOuterHTML(existingBlock, html);
                        } else {
                            editor.selection.moveToBookmark(bookmark);
                            editor.insertContent(html + "<p><br></p>");
                        }
                    });

                    editor.nodeChanged();
                    editor.setDirty(true);
                },
            });
        }

        editor.ui.registry.addButton("monument_carousel", {
            text: "Карусель",
            tooltip: "Вставить или изменить карусель",
            onAction: function () {
                openDialog(
                    findCarousel(editor.selection.getNode())
                );
            },
        });

        // Двойной щелчок по блоку открывает его настройки.
        editor.on("dblclick", function (event) {
            const block = findCarousel(event.target);

            if (block) {
                openDialog(block);
            }
        });

        // Стили только для предпросмотра внутри редактора.
        editor.on("init", function () {
            editor.dom.addStyle(`
                .monument-carousel {
                    border: 2px dashed #6688aa;
                    background: #f3f6fa;
                    padding: 16px;
                    margin: 24px 0;
                    cursor: pointer;
                }

                .monument-carousel::before {
                    content: "Карусель — двойной щелчок для изменения";
                    display: block;
                    margin-bottom: 12px;
                    font: 14px Arial, sans-serif;
                    color: #345;
                }

                .monument-carousel figure {
                    display: inline-block;
                    vertical-align: top;
                    width: 150px;
                    margin: 0 12px 12px 0;
                }

                .monument-carousel img {
                    width: 150px;
                    height: 100px;
                    object-fit: cover;
                }

                .monument-carousel figcaption {
                    font-size: 12px;
                    line-height: 1.4;
                    overflow-wrap: anywhere;
                }
            `);
        });
    });
})();