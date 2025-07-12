from fpdf import FPDF
from datetime import datetime

class ProjectReportPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "WeatherApp with Firebase Authentication", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, "Final Internship Project Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, "L", 1)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = ProjectReportPDF()
pdf.add_page()

sections = {
    "1. Project Overview": (
        "The WeatherApp with Firebase Authentication is an Android application developed as part of a final internship "
        "project at ApexPlanet Software Pvt Ltd. The app allows users to securely log in via Firebase Authentication and "
        "fetch real-time weather data using the OpenWeatherMap API."
    ),
    "2. Objectives": (
        "- Implement Firebase Authentication for secure user login.\n"
        "- Fetch real-time weather using Retrofit and OpenWeatherMap API.\n"
        "- Display weather data (temperature, humidity, conditions) in a user-friendly interface."
    ),
    "3. Technologies Used": (
        "• Java & Android Studio\n"
        "• Firebase Authentication\n"
        "• Retrofit & Gson\n"
        "• LiveData, ViewModel\n"
        "• ConstraintLayout, Material Design"
    ),
    "4. Features Implemented": (
        "- User Sign Up & Login (Email/Password)\n"
        "- Weather Data by City Input\n"
        "- Clean UI with Material Design Components\n"
        "- Error Handling & Loading States\n"
        "- Live Data Display of Weather Info"
    ),
    "5. Testing and Deployment": (
        "- Manual Testing on Emulator and Android Device\n"
        "- APK built using Android Studio\n"
        "- Optional release via GitHub Releases or Google Play Console"
    ),
    "6. Conclusion": (
        "This project enhanced understanding of full-stack Android development by integrating Firebase Authentication and "
        "third-party APIs. It provided hands-on experience with modern Android libraries and practices."
    ),
    "7. Submitted By": (
        "Name: Akash E\n"
        "Company: ApexPlanet Software Pvt Ltd\n"
        f"Date: {datetime.now().strftime('%B %d, %Y')}"
    )
}

for title, content in sections.items():
    pdf.chapter_title(title)
    pdf.chapter_body(content)

pdf.output("SUBMITTED_BY_AKASH_E_WeatherApp_Project_Report.pdf")
