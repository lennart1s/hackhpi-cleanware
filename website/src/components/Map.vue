<!-- eslint-disable -->
<template>
  <div :id="`chartdiv${_uid}`" style="width:100%;height:600px"></div>
</template>

<script>
/* eslint-disable */

export default {
  name: 'Map',
  data: () => ({
    destinationCities: [],
    destinationSeries: null,
    lineSeriesData: [],
    lineSeries: null,
  }),
  methods: {
 addDc(long, lat, n) {
   const that = this;
    that.$emit('dcCreated', { long, lat, n });
  this.destinationCities.push({
    n,
    id: `dc${n}`,
    title: `DataCenter ${n}`,
    geometry: { type: "Point", coordinates: [long, lat] }
  },);
  this.destinationSeries.data.setAll(this.destinationCities);

    this.destinationCities.forEach(function ({id}) {
      if (id !== `dc${n}`) {
    var destinationDataItem = that.destinationSeries.getDataItemById(id);

    that.lineSeriesData.push(that.lineSeries.pushDataItem({
      geometry: {
        type: "LineString",
        coordinates: [
          [long, lat],
          [
            destinationDataItem.get("longitude"),
            destinationDataItem.get("latitude")
          ]
        ]
      }
    }));
  }
    // this.lineSeries.data.setAll(this.lineSeriesData);
  });
}
  },
  mounted() {
    const that = this;
var root = am5.Root.new(`chartdiv${this._uid}`);

// Set themes
// https://www.amcharts.com/docs/v5/concepts/themes/
root.setThemes([
  am5themes_Animated.new(root)
]);

// Create the map chart
// https://www.amcharts.com/docs/v5/charts/map-chart/
var chart = root.container.children.push(
  am5map.MapChart.new(root, {
    panX: "translateX",
    panY: "translateY",
    projection: am5map.geoMercator()
  })
);

// Add labels and controls
var cont = chart.children.push(
  am5.Container.new(root, {
    layout: root.horizontalLayout,
    x: 20,
    y: 40
  })
);

cont.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Map"
  })
);

var mode = chart.children.push(
  am5.Container.new(root, {
    layout: root.horizontalLayout,
    x: 20,
    y: 80
  })
)

mode.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Inspect"
  })
);

var addMode = false;

var switchButton2 = mode.children.push(
  am5.Button.new(root, {
    themeTags: ["switch"],
    centerY: am5.p50,
    icon: am5.Circle.new(root, {
      themeTags: ["icon"]
    })
  })
);

mode.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Add"
  })
);

var switchButton = cont.children.push(
  am5.Button.new(root, {
    themeTags: ["switch"],
    centerY: am5.p50,
    icon: am5.Circle.new(root, {
      themeTags: ["icon"]
    })
  })
);


cont.children.push(
  am5.Label.new(root, {
    centerY: am5.p50,
    text: "Globe"
  })
);

switchButton.on("active", function () {
  if (!switchButton.get("active")) {
    chart.set("projection", am5map.geoMercator());
    chart.set("panX", "translateX");
    chart.set("panY", "translateY");
  } else {
    chart.set("projection", am5map.geoOrthographic());
    chart.set("panX", "rotateX");
    chart.set("panY", "rotateY");
  }
});

// Create main polygon series for countries
// https://www.amcharts.com/docs/v5/charts/map-chart/map-polygon-series/
var polygonSeries = chart.series.push(
  am5map.MapPolygonSeries.new(root, {
    geoJSON: am5geodata_worldLow
  })
);

var graticuleSeries = chart.series.push(am5map.GraticuleSeries.new(root, {}));
graticuleSeries.mapLines.template.setAll({
  stroke: root.interfaceColors.get("alternativeBackground"),
  strokeOpacity: 0.08
});

// Create line series for trajectory lines
// https://www.amcharts.com/docs/v5/charts/map-chart/map-line-series/
this.lineSeries = chart.series.push(am5map.MapLineSeries.new(root, {}));
this.lineSeries.mapLines.template.setAll({
  stroke: root.interfaceColors.get("alternativeBackground"),
  strokeOpacity: 0.6
});

// Create point series for markers
// https://www.amcharts.com/docs/v5/charts/map-chart/map-point-series/

// destination series
this.destinationSeries = chart.series.push(am5map.MapPointSeries.new(root, {}));

this.destinationSeries.bullets.push(function () {
  var circle = am5.Circle.new(root, {
    radius: 7,
    tooltipText: "{title}",
    tooltipY: 0,
    fill: am5.color(0xffba00),
    stroke: root.interfaceColors.get("background"),
    strokeWidth: 2
  });

  circle.events.on("click", function (e) {
    that.$emit('dcClicked', e.target.dataItem.dataContext.n);
    // selectOrigin(e.target.dataItem.get("id"));
  });

  return am5.Bullet.new(root, {
    sprite: circle
  });
});

// var button = root.container.children.push(
//   am5.Button.new(root, {
//     x: am5.p50,
//     y: 60,
//     centerX: am5.p50,
//     label: am5.Label.new(root, {
//       text: "Add new",
//       centerY: am5.p50
//     }),
//   })
// );

this.destinationSeries.data.setAll(this.destinationCities);

var planeSeries = chart.series.push(am5map.MapPointSeries.new(root, {}));

var plane = () => am5.Picture.new(root, {
        // svgPath:
        //     "m2,106h28l24,30h72l-44,-133h35l80,132h98c21,0 21,34 0,34l-98,0 -80,134h-35l43,-133h-71l-24,30h-28l15,-47",
        scale: 0.03,
        centerY: am5.p50,
        centerX: am5.p50,
        fill: am5.color(0x000000),
        rotation: 45,
        src: 'data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNzUycHQiIGhlaWdodD0iNzUycHQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDc1MiA3NTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiA8cGF0aCBkPSJtMzc2LjQxIDE2OC44OWMtMC4zOTA2Mi0wLjAxMTcxOS0wLjc4NTE2LTAuMDAzOTA2LTEuMTc1OCAwLjAyMzQzNy0xLjc4NTIgMC4xMzY3Mi0zLjUxOTUgMC42NzE4OC01LjA2NjQgMS41NzQybC0xNjguMzQgOTcuNjI5Yy0zLjYyNSAyLjEyNS01Ljg1MTYgNi4wMTU2LTUuODQ3NyAxMC4yMTloLTAuMDkzNzV2MTkzLjIzYy0wLjg0Mzc1IDQuOTYwOSAxLjUzOTEgOS45MTQxIDUuOTQxNCAxMi4zNDhsMTY4LjM0IDk3LjYwNWMzLjY3NTggMi4xMzI4IDguMjEwOSAyLjEzMjggMTEuODg3IDBsMTY4LjMyLTk3LjYwNWM0LjA0My0yLjM0MzggNi4zMzItNi44NDM4IDUuODUxNi0xMS40OTJ2LTE5My4zNGMwLjI3MzQ0LTQuNDY0OC0xLjk4ODMtOC43MDctNS44NTE2LTEwLjk2MWwtMTY4LjMyLTk3LjYyOWMtMS43MTg4LTAuOTk2MDktMy42NTYyLTEuNTQ2OS01LjY0NDUtMS41OTc3em0tMC4zMDA3OCAyNS40NjEgMTQ0LjczIDgzLjk4OC0xNDQuNzMgODMuOTg4LTE0NC43My04My45ODh6bS0wLjE4MzU5IDI0LjExN2MtNi41MzkxIDAuMDc4MTI1LTExLjc3NyA1LjQ0MTQtMTEuNjk5IDExLjk4djIzLjY4LTAuMDAzOTA2Yy0wLjA3NDIxOCAzLjE4NzUgMS4xNDQ1IDYuMjY5NSAzLjM3MTEgOC41NDY5IDIuMjI2NiAyLjI3NzMgNS4yODEyIDMuNTYyNSA4LjQ2ODggMy41NjI1IDMuMTgzNiAwIDYuMjM4My0xLjI4NTIgOC40NjQ4LTMuNTYyNSAyLjIzMDUtMi4yNzczIDMuNDQ1My01LjM1OTQgMy4zNzUtOC41NDY5di0yMy42NzZjMC4wMzUxNTYtMy4xOTE0LTEuMjE0OC02LjI1NzgtMy40Njg4LTguNTExN3MtNS4zMjQyLTMuNTAzOS04LjUxMTctMy40Njg4em0wIDcwLjk5MmMtMC40MTAxNiAwLjAwMzkwNi0wLjgxNjQxIDAuMDI3MzQzLTEuMjI2NiAwLjA3MDMxMi02LjA1MDggMC43MDMxMi0xMC41ODYgNS44ODY3LTEwLjQ3MyAxMS45OHYyMy42OC0wLjAwMzkwNmMwLjE0NDUzIDYuNDM3NSA1LjQwMjMgMTEuNTc4IDExLjg0IDExLjU3OCA2LjQzMzYgMCAxMS42OTUtNS4xNDA2IDExLjg0LTExLjU3OHYtMjMuNjhjMC4wNTQ2ODgtMy4xOTkyLTEuMTg3NS02LjI4NTItMy40NDUzLTguNTU0Ny0yLjI1MzktMi4yNjk1LTUuMzM1OS0zLjUzMTItOC41MzUyLTMuNDkyMnptMTU2LjcxIDkuMzg2N3YxNjcuOTNsLTE0NC43MyA4My45NjV2LTE2Ny44NnptLTMxMy4wNSAwLjAyMzQzOCAxNDQuNjQgODMuOTY1djE2Ny44NmwtMTQ0LjY0LTgzLjkxOHptMTA2LjE5IDk0LjY2OHYwLjAwMzkwN2MtMi4yODEyLTAuMDU4NTk0LTQuNTI3MyAwLjU0Mjk3LTYuNDcyNyAxLjczNDRsLTIwLjQ0MSAxMS43OTNjLTUuNjc5NyAzLjI4MTItNy42MjExIDEwLjU0My00LjMzNTkgMTYuMjE5IDMuMjgxMiA1LjY3OTcgMTAuNTQzIDcuNjIxMSAxNi4yMTkgNC4zMzU5bDIwLjQ0MS0xMS44ODd2MC4wMDM5MDdjNC42NzU4LTIuNTg1OSA3LjA0My03Ljk4MDUgNS43NzczLTEzLjE2OHMtNS44NDc3LTguODkwNi0xMS4xODgtOS4wMzEyem0xMDEuMDcgMC40Mzc1djAuMDAzOTA3Yy01LjI4NTIgMC4yNjU2Mi05Ljc1IDQuMDExNy0xMC45MzggOS4xNjgtMS4xODc1IDUuMTYwMiAxLjE5MTQgMTAuNDggNS44MjgxIDEzLjAzMWwyMC41MzUgMTEuODg3YzIuNzIyNyAxLjg0MzggNi4wODk4IDIuNDY4OCA5LjI5NjkgMS43MzA1IDMuMjAzMS0wLjczODI4IDUuOTU3LTIuNzc3MyA3LjU5NzctNS42MjUgMS42NDQ1LTIuODUxNiAyLjAyNzMtNi4yNTM5IDEuMDU4Ni05LjM5ODQtMC45Njg3NS0zLjE0MDYtMy4xOTkyLTUuNzQyMi02LjE2MDItNy4xNzE5bC0yMC40NDEtMTEuODg3Yy0xLjY5MTQtMS4wMzkxLTMuNjEzMy0xLjYzMjgtNS41OTc3LTEuNzM0NC0wLjM5MDYzLTAuMDE5NTMxLTAuNzg1MTYtMC4wMTk1MzEtMS4xNzk3IDB6bS0xNjIuMjYgMzUuMTcydjAuMDAzOTA2Yy0wLjQ5MjE5LTAuMDE1NjI1LTAuOTg0MzggMC0xLjQ3NjYgMC4wNDI5NjgtMS44NTk0IDAuMTM2NzItMy42NTYyIDAuNzA3MDMtNS4yNSAxLjY2OGwtMjAuNDQxIDExLjg4N3YtMC4wMDM5MDZjLTUuNTM5MSAzLjM0MzgtNy4zNzg5IDEwLjUwNC00LjE0MDYgMTYuMTA1IDMuMjQyMiA1LjU5NzcgMTAuMzY3IDcuNTY2NCAxNi4wMjcgNC40Mjk3bDIwLjQ0MS0xMS44ODNjNC42ODc1LTIuNTM1MiA3LjEwMTYtNy44OTQ1IDUuODk4NC0xMy4wOS0xLjIwMzEtNS4xOTE0LTUuNzMwNS04Ljk0MTQtMTEuMDU5LTkuMTU2MnptMjI0Ljg2IDAuNDYwOTR2MC4wMDM5MDZjLTAuMzk4NDQtMC4wMTE3MTktMC44MDA3OC0wLjAwMzkwNi0xLjIwMzEgMC4wMjM0MzgtNS4yNzczIDAuMjg1MTYtOS43MjY2IDQuMDM5MS0xMC45MDIgOS4xOTE0LTEuMTc1OCA1LjE1MjMgMS4yMDcgMTAuNDYxIDUuODM5OCAxMy4wMDhsMjAuNTM1IDExLjg4N2MyLjcyNjYgMS42NTIzIDYgMi4xMzY3IDkuMDg5OCAxLjM0MzggMy4wODk4LTAuNzg5MDYgNS43MjY2LTIuNzg5MSA3LjMyNDItNS41NDY5IDEuNTk3Ny0yLjc2MTcgMi4wMTU2LTYuMDQ2OSAxLjE2NDEtOS4xMTcyLTAuODUxNTYtMy4wNzAzLTIuOTAyMy01LjY3MTktNS42OTUzLTcuMjE0OGwtMjAuNTMxLTExLjg4M2MtMS43MDMxLTEuMDI3My0zLjYzNjctMS42MDU1LTUuNjIxMS0xLjY4NzV6Ii8+Cjwvc3ZnPgo=',
    });

function sendRandPack() {
  // console.log(this.lineSeriesData);
  const di = that.lineSeriesData[Math.floor(Math.random()*that.lineSeriesData.length)];
  planeSeries.bullets.push(function () {
        var container = am5.Container.new(root, {});
        container.children.push(plane());
        return am5.Bullet.new(root, { sprite: container });
    });
  var planeDataItem = planeSeries.pushDataItem({
        lineDataItem: di,
        positionOnLine: 0,
        autoRotate: true,
    });

    const dur = 2000;
    console.log
    planeDataItem.animate({
        key: 'positionOnLine',
        to: 1,
        duration: dur*2,
        loops: Infinity,
        easing: am5.ease.yoyo(am5.ease.linear),
    });
    setTimeout(() => planeDataItem.hide(), dur-500);
}

var button = root.container.children.push(
  am5.Button.new(root, {
    x: am5.p50,
    y: 60,
    centerX: am5.p50,
    label: am5.Label.new(root, {
      text: "Run cycle",
      centerY: am5.p50
    }),
  })
);

button.events.on("click", function () {
  sendRandPack();
});
// button.events.on("click", function () {
//   addDest(4.3676, 50.8371);
// });

var dcs = -1;

chart.events.on("click", function(ev){
  // $('#tempInfo').html(event.mapObject.infoTitle); // Changes with clicking
  const { longitude: long, latitude: lat } = chart.invert(ev.point);
  if (switchButton2.get("active")) {
    dcs++;
    if (dcs > 0) that.addDc(long, lat, dcs);
  }
});

function selectOrigin(id) {
  currentId = id;
  var dataItem = originSeries.getDataItemById(id);
  var dataContext = dataItem.dataContext;
  chart.zoomToGeoPoint(dataContext.zoomPoint, dataContext.zoomLevel, true);

  var destinations = dataContext.destinations;
  var lineSeriesData = [];
  var originLongitude = dataItem.get("longitude");
  var originLatitude = dataItem.get("latitude");

  // am5.array.each(destinations, function (did) {
  //   var destinationDataItem = destinationSeries.getDataItemById(did);
  //   if (!destinationDataItem) {
  //     destinationDataItem = originSeries.getDataItemById(did);
  //   }
  //   lineSeriesData.push({
  //     geometry: {
  //       type: "LineString",
  //       coordinates: [
  //         [originLongitude, originLatitude],
  //         [
  //           destinationDataItem.get("longitude"),
  //           destinationDataItem.get("latitude")
  //         ]
  //       ]
  //     }
  //   });
  // });
  this.lineSeries.data.setAll(this.lineSeriesData);
}

var currentId = "london";

this.destinationSeries.events.on("datavalidated", function () {
  // selectOrigin(currentId);
  chart.zoomToGeoPoint({ longitude: -20.1341, latitude: 49.1712 }, 2.74, true);
});

// Make stuff animate on load
chart.appear(1000, 100);
  }
};
</script>

<style scoped lang="stylus">

</style>
