import { useState } from "react"
import axios from "axios"

import {
  BarChart3,
  Users,
  Brain,
  AlertTriangle
} from "lucide-react"

import { motion } from "framer-motion"

export default function Dashboard() {

  const [formData, setFormData] = useState({

    Age: 35,
    Department: "Sales",
    JobRole: "Sales Executive",
    MonthlyIncome: 5000,
    YearsAtCompany: 3,
    JobSatisfaction: 2,
    OverTime: "Yes",
    WorkLifeBalance: 2
  })

  const [result, setResult] = useState(null)

  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]: e.target.value
    })
  }

  const analyzeEmployee = async () => {

    try {

      const API_BASE = import.meta.env.VITE_API_URL || 'https://accurateandconsistentmodel-verdictalign-9.onrender.com/api/v1';

      const response = await axios.post(
  `${API_BASE}/predict`,

        formData
      )

      setResult(response.data)

    } catch (error) {

      console.log(error)
    }
  }

  return (

    <div className="min-h-screen bg-darkbg text-white flex">

      {/* SIDEBAR */}

      <div className="w-64 bg-secondary p-6 border-r border-slate-700">

        <h1 className="text-3xl font-bold text-primary">

          VerdictAlign
        </h1>

        <p className="text-slate-400 mt-1">
          Hybrid AI Decision Engine
        </p>

        <div className="mt-10 space-y-6">

          <div className="flex items-center gap-3">
            <BarChart3 size={20} />
            <span>Dashboard</span>
          </div>

          <div className="flex items-center gap-3">
            <Users size={20} />
            <span>Employee Analysis</span>
          </div>

          <div className="flex items-center gap-3">
            <Brain size={20} />
            <span>Explainability</span>
          </div>

          <div className="flex items-center gap-3">
            <AlertTriangle size={20} />
            <span>Consistency</span>
          </div>

        </div>
      </div>

      {/* MAIN CONTENT */}

      <div className="flex-1 p-10">

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
        >

          <h1 className="text-4xl font-bold">

            Employee Attrition Analysis
          </h1>

          <p className="text-slate-400 mt-2">

            AI-driven hybrid employee intelligence platform
          </p>

        </motion.div>

        {/* FORM */}

        <motion.div

          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}

          className="mt-10 bg-cardbg rounded-3xl p-8 shadow-2xl border border-slate-700"
        >

          <div className="grid grid-cols-2 gap-6">

            <input
              name="Age"
              placeholder="Age"
              value={formData.Age}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="Department"
              placeholder="Department"
              value={formData.Department}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="JobRole"
              placeholder="Job Role"
              value={formData.JobRole}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="MonthlyIncome"
              placeholder="Monthly Income"
              value={formData.MonthlyIncome}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="YearsAtCompany"
              placeholder="Years At Company"
              value={formData.YearsAtCompany}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="JobSatisfaction"
              placeholder="Job Satisfaction"
              value={formData.JobSatisfaction}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="OverTime"
              placeholder="OverTime"
              value={formData.OverTime}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

            <input
              name="WorkLifeBalance"
              placeholder="Work Life Balance"
              value={formData.WorkLifeBalance}
              onChange={handleChange}
              className="bg-slate-800 p-4 rounded-xl"
            />

          </div>

          <button

            onClick={analyzeEmployee}

            className="mt-8 bg-primary hover:bg-blue-700 transition-all px-8 py-4 rounded-2xl font-bold"
          >

            Analyze Employee

          </button>

        </motion.div>

        {/* RESULT */}

        {result && (

          <motion.div

            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}

            className="mt-10 grid grid-cols-2 gap-6"
          >

            <div className="bg-cardbg p-8 rounded-3xl border border-slate-700">

              <h2 className="text-2xl font-bold">
                Prediction Result
              </h2>

              <div className="mt-6">

                <p className="text-slate-400">
                  Attrition Prediction
                </p>

                <h1 className="text-5xl font-bold mt-2">

                  {result.prediction}

                </h1>

                <p className="mt-4 text-accent text-xl">

                  Confidence:
                  {" "}
                  {(result.probability * 100).toFixed(0)}%

                </p>

              </div>
            </div>

            <div className="bg-cardbg p-8 rounded-3xl border border-slate-700">

              <h2 className="text-2xl font-bold">
                Decision Validation
              </h2>

              <div className="mt-6">

                <p className="text-xl">

                  {result.consistency_status.status}

                </p>

                <p className="text-slate-400 mt-4">

                  Historical Majority:
                  {" "}
                  {result.expected_behavior.majority_vote}

                </p>

                <p className="text-slate-400 mt-2">

                  Similar Cases:
                  {" "}
                  {result.expected_behavior.similar_cases}

                </p>

              </div>
            </div>

          </motion.div>
        )}

      </div>
    </div>
  )
}