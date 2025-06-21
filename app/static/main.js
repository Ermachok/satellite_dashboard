const map = L.map("map").setView([50, 35], 5);

// Базовый слой OpenStreetMap
const baseLayers = {
  "OpenStreetMap": L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map)
};

// Дата (по умолчанию сегодняшняя)
let date = new Date().toISOString().slice(0, 10);

// Слои с их id для бекенда
const layers = {
  "True Color (Terra)": "clouds",  // карта бекенда показывает clouds для MODIS_Terra_Cloud_FR
  "Fires": "fires",
  "Clouds": "clouds",
  "NO2": "no2",
  "CO": "co"
};

const overlayLayers = {};

for (const [label, layerId] of Object.entries(layers)) {
  const tileLayer = L.tileLayer(
    `/tiles/${layerId}?date=${date}&z={z}&x={x}&y={y}`,
    {
      maxZoom: 9,
      attribution: `NASA GIBS — ${label}`
    }
  );
  overlayLayers[label] = tileLayer;
}

// Добавляем на карту первый слой
overlayLayers["True Color (Terra)"].addTo(map);

// Контрол слоёв
L.control.layers(baseLayers, overlayLayers).addTo(map);
