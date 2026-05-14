import "./App.css";
import axios from "axios";
import { useState } from "react";

import {
  FaChartBar,
  FaUserFriends,
  FaBrain,
  FaShieldAlt,
  FaCog
} from "react-icons/fa";

function App() {

  const [formData, setFormData] = useState({
    Age: 35,
    Department: "Sales",
    JobRole: "Sales Executive",
    MonthlyIncome: 5000,
    YearsAtCompany: 3,
    JobSatisfaction: 2,
    OverTime: "Yes",
    WorkLifeBalance: 2,
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const analyzeEmployee = async () => {

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        formData
      );

      setResult(response.data);

    } catch (err) {
      console.log(err);
      alert("Backend Error");
    }
  };

  return (

    <div className="dashboard">

      {/* SIDEBAR */}

      <div className="sidebar">

        <div>
          <h1>VerdictAlign</h1>
          <p>Hybrid AI Decision Engine</p>
        </div>

        <div className="menu">

          <div className="menu-item active">
            <FaChartBar />
            Dashboard
          </div>

          

        </div>

      </div>

      {/* MAIN CONTENT */}

      <div className="main">

        <div className="topbar">

          <div>
            <h2>Employee Attrition Consistency Analysis</h2>

            <span>
              Analyze employee attrition risk using predictive AI,
              semantic similarity retrieval, and explainable validation.
            </span>
          </div>

        </div>

        <div className="main-layout">

          {/* LEFT */}

          <div className="left-panel">

            <div className="form-card">

              <div className="form-grid">
              
              <div className="input-group">
                <label>Age</label>
                <input
                  type="number"
                  name="Age"
                  placeholder="Age"
                  value={formData.Age}
                  onChange={handleChange}
                />
                </div>

                <div className="input-group">
                 <label>Department</label>
                <select
                  name="Department"
                  value={formData.Department}
                  onChange={handleChange}
                >
                  <option>Sales</option>
                  <option>Research & Development</option>
                  <option>Human Resources</option>
                  <option>Finance</option>
                  <option>IT</option>
                  <option>Management</option>
                  <option>Marketing</option>
                  <option>Product Management</option>
                  <option>others</option>
                </select>
                </div>


                <div className="input-group">
                <label>Job Role</label>
                <select
                  name="JobRole"
                  value={formData.JobRole}
                  onChange={handleChange}
                >
                  <option>Sales Executive</option>
                  <option>Research Scientist</option>
                  <option>Laboratory Technician</option>
                  <option>Manager</option>
                  <option>Software Engineer</option>
                  <option>Research Analyst</option>
                  <option>Senior Developer</option>
                  <option>Data Structure Engineer</option>
                  <option>Sales Representative</option>
                  <option>Research Director</option>
                  <option>Human Resources</option>
                  <option>Manufacturing Director</option>
                  <option>Healthcare Representative</option>
                  <option>Technical Author</option>
                  <option>others</option>
                </select>
                </div>

                <div className="input-group">
                <label>Monthly Income</label>
                <input
                  type="number"
                  name="MonthlyIncome"
                  placeholder="Monthly Income"
                  value={formData.MonthlyIncome}
                  onChange={handleChange}
                />
                </div>

                <div className="input-group">
  <label>Years at Company</label>
  <input
    type="number"
    name="YearsAtCompany"
    placeholder="e.g. 3"
    value={formData.YearsAtCompany}
    onChange={handleChange}
  />
</div>

                <select
                  name="JobSatisfaction"
                  value={formData.JobSatisfaction}
                  onChange={handleChange}
                >
                  <option value="1">Job Satisfaction 1</option>
                  <option value="2">Job Satisfaction 2</option>
                  <option value="3">Job Satisfaction 3</option>
                  <option value="4">Job Satisfaction 4</option>
                </select>

                <div className="input-group">
  <label>OverTime</label>
  <select
    name="OverTime"
    value={formData.OverTime}
    onChange={handleChange}
  >
    <option value="Yes">Yes</option>
    <option value="No">No</option>
  </select>
</div>

                <select
                  name="WorkLifeBalance"
                  value={formData.WorkLifeBalance}
                  onChange={handleChange}
                >
                  <option value="1">Work Life Balance 1</option>
                  <option value="2">Work Life Balance 2</option>
                  <option value="3">Work Life Balance 3</option>
                  <option value="4">Work Life Balance 4</option>
                </select>

              </div>

              <button onClick={analyzeEmployee}>
                Analyze Employee
              </button>

            </div>

            {/* RESULT */}

            {result && (

              <div className="result-card">

                <div className="result-row">

                  <div>
                    <h4>Prediction</h4>
                    <p className="risk">
                      {result.prediction}
                    </p>
                  </div>

                  <div>
                    <h4>Consistency</h4>
                    <p>
                      {result.consistency_status.status}
                    </p>
                  </div>

                  <div>
                    <h4>Confidence</h4>
                    <p>
                      {(result.consistency_status.confidence * 100).toFixed(1)}%
                    </p>
                  </div>

                </div>

              </div>

            )}

          </div>

          {/* RIGHT */}

          <div className="right-panel">

            <div className="metric-card">
              <h3>Attrition Risk</h3>
              <p>
                {result
                  ? `${(result.probability * 100).toFixed(1)}%`
                  : "0%"}
              </p>
            </div>

            <div className="metric-card">
              <h3>Historical Match</h3>
              <p>
                {result
                  ? result.expected_behavior.majority_vote
                  : "-"}
              </p>
            </div>

            <div className="metric-card">
              <h3>Consistency</h3>
              <p>
                {result
                  ? result.consistency_status.status
                  : "-"}
              </p>
            </div>

            <div className="metric-card">
              <h3>Similarity Cases</h3>
              <p>
                {result
                  ? result.expected_behavior.similar_cases
                  : "-"}
              </p>
            </div>

          </div>
          

        </div>

        {result?.explanation && (
  <div className="explanation-card">

    <h2>SHAP Explainability</h2>

    <div className="feature-list">

      {result.explanation.map((item, index) => (
        <div className="feature-item" key={index}>

          <div className="feature-name">
            {item[0]}
          </div>

          <div className="feature-value">
            {item[1].toFixed(3)}
          </div>

        </div>
      ))}

    </div>

  </div>
)}

      </div>

    </div>
  );
}

export default App;