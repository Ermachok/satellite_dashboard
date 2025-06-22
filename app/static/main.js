const map = L.map("map").setView([50, 35], 5);


const baseLayers = {
  "OpenStreetMap": L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution: "&copy; OpenStreetMap contributors"
  }).addTo(map),
};


const date = new Date().toISOString().slice(0, 10);

const layers = {
  "Clouds": "clouds",
  "Fires": "fires",
  "NO2": "no2",
  "CO": "co",
};

const overlayLayers = {};

for (const [label, id] of Object.entries(layers)) {
  const tileLayer = L.tileLayer(
    `/api/tiles/${id}/{z}/{x}/{y}.jpg?date=${date}`,
    {
      maxZoom: 9,
      opacity: 0.4,
      attribution: `NASA GIBS — ${label}`,
    }
  );
  overlayLayers[label] = tileLayer;
}

overlayLayers["Clouds"].addTo(map);

L.control.layers(baseLayers, overlayLayers).addTo(map);
