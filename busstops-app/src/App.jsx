import React, {useState} from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { Alert, Spinner } from "react-bootstrap";
import "./App.css";
import useSWR from "swr";

const fetcher = (url) => fetch(url).then((r) => r.json());
function App() {
    const [activeStop, setActiveStop] = useState(null);
    const position = [-1.285, 36.821];
    const zoom = 16;
    const url = import.meta.env.VITE_GEO_API;
    const { data, error } = useSWR(url, fetcher);
    if (error) {
    return <Alert variant="danger">There is a problem</Alert>;
  }
    if (!data) {
    return (
      <Spinner
        animation="border"
        variant="danger"
        role="status"
        style={{
          width: "400px",
          height: "400px",
          margin: "auto",
          display: "block",
        }}
      />
    );
  }
  const busstops = data && !error ? data : {};
    return (
        <>
            <h1>Nairobi Bus Stops</h1>
            <MapContainer center={position} zoom={zoom} scrollWheelZoom={false}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    />
                {busstops.features.map((stop) => (
                    <Marker key={stop.properties.stop_id}
                    position={[stop.properties.stop_lat, stop.properties.stop_lon]}
                    onClick={() => {
              setActiveStop(stop);
            }}>
                        <Popup>
                            <div>
                                <p>{stop.properties.stop_name}</p>
                            </div>
                        </Popup>
                    </Marker>
                ))}
      </MapContainer>
            </>
  );
}

export default App;
