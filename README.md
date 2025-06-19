# Smart Budget Allocator 💰

**Smart Budget Allocator** is a web application that intelligently selects a subset of expenses within a given budget using a dynamic programming-based Subset Sum algorithm. It features a clean UI, responsive design, dark mode, expense visualization with charts, and PDF export functionality.

---

## 🚀 Features

- Input a total budget and a list of potential expenses  
- Optimally allocate budget using a Subset Sum algorithm  
- Visualize results with interactive pie charts (Chart.js)  
- Toggle between light and dark mode  
- Export a budget report (including charts) as a PDF (using jsPDF)  
- Responsive design suitable for mobile and desktop

---

## 🛠️ Tech Stack

- **Frontend:**  
  - HTML — structured forms and layout  
  - CSS (SASS-compatible) — styling, responsiveness, and dark mode  
  - JavaScript — form handling, chart rendering, PDF export  
- **Backend:**  
  - Python + Flask — API endpoints, core logic  
  - Dynamic programming — Subset Sum algorithm implementation  
- **Libraries:**  
  - Chart.js — data visualization  
  - jsPDF — exporting visuals and data to PDF

---



## ✅ Progress Overview

The **Smart Budget Allocator** project is in an advanced stage, with around **90% of the total work completed**. The key components — including user interface design, backend logic implementation, and frontend-backend integration — have all been successfully developed and tested collaboratively by the team.

- **Frontend work** (HTML, CSS, and JavaScript) is complete, offering a clean UI with features such as a dark mode toggle, chart visualization, and toast notifications.  
- The **backend**, developed using Flask, handles budget allocation logic via a subset sum dynamic programming algorithm, and returns optimized results seamlessly to the frontend.  
- **Data visualization** is handled through Chart.js, and **PDF export functionality** is implemented using jsPDF, which allows users to download a detailed report of their budget allocation along with the pie chart.

The remaining tasks primarily include final UI adjustments for better mobile responsiveness, thorough edge-case testing, and deployment to a live environment. The entire team has worked in coordination, ensuring no component is delayed. Backend logic and frontend integration were completed slightly ahead of schedule, which has allowed more time for polishing and validation.

Overall, the project is **on track**, and we anticipate completing the final testing and deployment comfortably within the timeline.

---

## 📂 Project Structure

```
smart-budget-allocator/
├── backend/
│   ├── app.py               # Flask application and route handling
│   └── subset.py            # Dynamic programming subset-sum logic
├── frontend/
│   ├── index.html           # Main UI structure
│   ├── style.css            # Global styling + dark mode
│   └── script.js            # Chart and PDF export logic
└── README.md
```

---

## 🧪 Testing

| Test Type           | Status | Notes                                      |
|---------------------|--------|--------------------------------------------|
| Functionality Test  | ✅ Pass | Budget allocation and output are working   |
| UI Test             | ✅ Pass | Responsive design, dark mode toggle        |
| PDF Export Test     | ✅ Pass | Chart and data exported correctly to PDF   |
| Algorithm Accuracy  | ✅ Pass | Correct subset selected within budget      |

---


## 🚦 Getting Started

### Prerequisites

- Python 3.8+  
- Node.js + NPM (optional, for frontend automation)

### Setup & Run

```bash
# Clone repo
git clone https://github.com/your-org/smart-budget-allocator.git
cd smart-budget-allocator

# --- Backend setup ---
cd backend
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run

# --- Frontend setup ---
cd ../frontend
# Open index.html in your browser to use the app
```

---

## 📦 Build & Deployment

1. Ensure both backend and frontend are production-ready  
2. Choose a hosting platform (e.g., Heroku, Vercel, AWS)  
3. Set up required environment variables  
4. Deploy via Git or CI/CD  
5. Test live version on multiple devices

---

## 🤝 Contributions

Contributions are welcome! Please:

1. Fork this repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Make your changes  
4. Commit and push  
5. Open a pull request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 📧 Contact

- **Manya**,  – manyabidaliya@gmail.com
- **Rajni** – rajanijyala138@gmail.com
- **Mahi** – mahisharma22679@gmail.com  
- **Mudita** – muditachauhan24@gmail.com 

Made with ❤️ by the **CodeCents** team.
