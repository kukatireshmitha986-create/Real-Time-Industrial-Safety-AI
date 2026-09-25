import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [events, setEvents] = useState([]);
  const [totalViolations, setTotalViolations] = useState(0);
  const [backendStatus, setBackendStatus] = useState("Checking...");
  const [loading, setLoading] = useState(true);
  const [selectedImage, setSelectedImage] = useState(null);

  const fetchData = async () => {
    try {
      const healthResponse = await fetch(`${API_URL}/api/health`);

      if (!healthResponse.ok) {
        throw new Error("Backend unavailable");
      }

      const healthData = await healthResponse.json();

      setBackendStatus(
        healthData.status === "success" ? "Online" : "Offline"
      );

      const eventsResponse = await fetch(
        `${API_URL}/api/events/recent`
      );

      const eventsData = await eventsResponse.json();

      setEvents(eventsData.events || []);

      const countResponse = await fetch(
        `${API_URL}/api/events/count`
      );

      const countData = await countResponse.json();

      setTotalViolations(
        countData.total_violations || 0
      );

    } catch (error) {
      console.error(error);
      setBackendStatus("Offline");
    }

    setLoading(false);
  };

  useEffect(() => {
    fetchData();

    const interval = setInterval(fetchData, 5000);

    return () => clearInterval(interval);
  }, []);

  const getEvidenceUrl = (path) => {
    if (!path) return null;

    const filename = path
      .replace(/\\/g, "/")
      .split("/")
      .pop();

    return `${API_URL}/screenshots/${filename}`;
  };

  return (
    <div className="app">

      <header className="header">
        <div>
          <h1>Industrial Safety AI</h1>
          <p>
            AI-Powered Real-Time Safety Monitoring Dashboard
          </p>
        </div>

        <div className="status">
          <span
            className={
              backendStatus === "Online"
                ? "status-dot online"
                : "status-dot offline"
            }
          ></span>

          Backend: {backendStatus}
        </div>
      </header>

      <main className="container">

        <section className="stats">

          <div className="card">
            <div className="card-icon">🚨</div>
            <h3>Total Violations</h3>

            <div className="number">
              {totalViolations}
            </div>

            <p>Recorded safety events</p>
          </div>

          <div className="card">
            <div className="card-icon">📋</div>
            <h3>Recent Violations</h3>

            <div className="number">
              {events.length}
            </div>

            <p>Latest detected events</p>
          </div>

          <div className="card">
            <div className="card-icon">🤖</div>
            <h3>AI Detection</h3>

            <div className="number">
              LIVE
            </div>

            <p>YOLO11 real-time monitoring</p>
          </div>

        </section>

        <section className="monitoring-card">

          <div>
            <h2>Live Monitoring System</h2>
            <p>
              Real-time industrial safety violation detection
            </p>
          </div>

          <div className="live-status">
            <span className="pulse"></span>
            LIVE MONITORING
          </div>

        </section>

        <section className="events-section">

          <div className="section-header">

            <div>
              <h2>Recent Safety Violations</h2>
              <p>
                Latest events recorded by the AI monitoring system
              </p>
            </div>

            <button
              onClick={fetchData}
              className="refresh-button"
            >
              ↻ Refresh
            </button>

          </div>

          {loading ? (

            <div className="message">
              Loading safety events...
            </div>

          ) : events.length === 0 ? (

            <div className="message">
              No safety violations recorded yet.
            </div>

          ) : (

            <div className="table-container">

              <table>

                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Timestamp</th>
                    <th>Violation</th>
                    <th>Confidence</th>
                    <th>Status</th>
                    <th>Evidence</th>
                  </tr>
                </thead>

                <tbody>

                  {events.map((event) => {

                    const evidenceUrl =
                      getEvidenceUrl(
                        event.screenshot_path
                      );

                    return (
                      <tr key={event.id}>

                        <td>
                          <strong>
                            #{event.id}
                          </strong>
                        </td>

                        <td>
                          {event.timestamp}
                        </td>

                        <td>
                          <span className="violation">
                            ⚠ {event.violation_type}
                          </span>
                        </td>

                        <td>
                          {(event.confidence * 100).toFixed(1)}%
                        </td>

                        <td>
                          <span className="status-badge">
                            {event.status}
                          </span>
                        </td>

                        <td>

                          {evidenceUrl ? (

                            <button
                              className="evidence-button"
                              onClick={() =>
                                setSelectedImage(
                                  evidenceUrl
                                )
                              }
                            >
                              📸 View Evidence
                            </button>

                          ) : (

                            <span className="evidence">
                              No image
                            </span>

                          )}

                        </td>

                      </tr>
                    );
                  })}

                </tbody>

              </table>

            </div>
          )}

        </section>

        <section className="architecture">

          <h2>System Architecture</h2>

          <p className="architecture-subtitle">
            End-to-end AI safety monitoring pipeline
          </p>

          <div className="architecture-flow">

            <div className="architecture-box">
              📷 Webcam
            </div>

            <div className="arrow">→</div>

            <div className="architecture-box">
              🤖 YOLO11 AI
            </div>

            <div className="arrow">→</div>

            <div className="architecture-box">
              ⚠️ Violation Detection
            </div>

            <div className="arrow">→</div>

            <div className="architecture-box">
              🗄️ SQLite
            </div>

            <div className="arrow">→</div>

            <div className="architecture-box">
              ⚡ FastAPI
            </div>

            <div className="arrow">→</div>

            <div className="architecture-box">
              📊 React Dashboard
            </div>

          </div>

        </section>

        <section className="technologies">

          <h2>Technologies Used</h2>

          <div className="tech-grid">

            <div className="tech-item">Python</div>
            <div className="tech-item">YOLO11</div>
            <div className="tech-item">OpenCV</div>
            <div className="tech-item">SQLite</div>
            <div className="tech-item">FastAPI</div>
            <div className="tech-item">React</div>

          </div>

        </section>

      </main>

      <footer>

        <p>
          AI-Powered Real-Time Industrial Safety Monitoring System
        </p>

        <p>
          YOLO11 • OpenCV • SQLite • FastAPI • React
        </p>

      </footer>

      {selectedImage && (

        <div
          className="modal-overlay"
          onClick={() => setSelectedImage(null)}
        >

          <div
            className="modal"
            onClick={(e) => e.stopPropagation()}
          >

            <div className="modal-header">

              <h2>Safety Violation Evidence</h2>

              <button
                className="close-button"
                onClick={() => setSelectedImage(null)}
              >
                ✕
              </button>

            </div>

            <img
              src={selectedImage}
              alt="Safety violation evidence"
              className="evidence-image"
            />

            <button
              className="close-modal-button"
              onClick={() => setSelectedImage(null)}
            >
              Close
            </button>

          </div>

        </div>

      )}

    </div>
  );
}

export default App;
