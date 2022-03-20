/* eslint-disable */
// 2d/3d view

const viewContainer = chart.children.push(
  am5.Container.new(root, {
    layout: root.horizontalLayout,
    x: 20,
    y: 40
  })
);

viewContainer.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Map"
  })
);

var viewSwitchButton = viewContainer.children.push(
  am5.Button.new(root, {
    themeTags: ["switch"],
    centerY: am5.p50,
    icon: am5.Circle.new(root, {
      themeTags: ["icon"]
    })
  })
);

viewContainer.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Globe"
  })
);
