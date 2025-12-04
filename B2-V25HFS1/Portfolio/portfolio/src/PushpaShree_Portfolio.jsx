import React from "react";

// Single-file React component (Tailwind CSS required in your project)
// Usage: save as PushpaShree_Portfolio.jsx and import in your app (e.g. App.jsx)

export default function PushpaShreePortfolio() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-slate-50 text-slate-900">
      <header className="max-w-5xl mx-auto p-6 flex flex-col sm:flex-row items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 rounded-full bg-gradient-to-br from-indigo-500 to-purple-500 flex items-center justify-center text-white font-bold text-xl">
            PB
          </div>
          <div>
            <h1 className="text-2xl font-extrabold">Bellamkonda Pushpa Shree</h1>
            <p className="text-sm text-slate-600">B.Tech — Computer Science Engineering | CGPA: 8.8</p>
          </div>
        </div>

        <nav className="mt-4 sm:mt-0 flex gap-4">
          <a href="#projects" className="text-sm hover:underline">Projects</a>
          <a href="#skills" className="text-sm hover:underline">Skills</a>
          <a href="#education" className="text-sm hover:underline">Education</a>
          <a href="#contact" className="text-sm hover:underline">Contact</a>
        </nav>
      </header>

      <main className="max-w-5xl mx-auto px-6 pb-16">
        {/* Hero */}
        <section className="bg-white shadow-sm rounded-2xl p-6 md:p-10 mb-8">
          <div className="md:flex md:items-center md:justify-between">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold">Hi — I'm Pushpa Shree</h2>
              <p className="mt-3 text-slate-700 max-w-2xl">
                I am seeking a role in software development where I can apply my academic knowledge, problem-solving
                skills and passion for technology. I enjoy building practical systems—especially around AI, web apps and
                DevOps automation—and learning from experienced teams.
              </p>

              <div className="mt-5 flex flex-wrap gap-3">
                <a
                  href="mailto:pushpashreebellamkonda@gmail.com"
                  className="inline-flex items-center gap-2 rounded-full border px-4 py-2 text-sm hover:bg-slate-50"
                >
                  Email
                </a>
                <a
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-2 rounded-full border px-4 py-2 text-sm hover:bg-slate-50"
                >
                  GitHub
                </a>
                <a
                  href="https://www.linkedin.com/in/bellamkonda-pushpa-shree-916a89248/"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-2 rounded-full border px-4 py-2 text-sm hover:bg-slate-50"
                >
                  LinkedIn
                </a>
              </div>
            </div>

            <div className="mt-6 md:mt-0">
              <div className="w-56 h-56 rounded-2xl bg-gradient-to-br from-indigo-50 to-purple-50 flex items-center justify-center text-indigo-700 font-semibold text-sm p-4">
                <div>
                  <div className="text-xs text-slate-500">Phone</div>
                  <div className="mt-1">+91 9177394740</div>
                  <div className="mt-3 text-xs text-slate-500">Email</div>
                  <div className="mt-1 text-sm">pushpashreebellamkonda@gmail.com</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Skills + Summary */}
        <section id="skills" className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="md:col-span-2 bg-white rounded-2xl p-6 shadow-sm">
            <h3 className="text-lg font-semibold">Profile</h3>
            <p className="mt-3 text-slate-700">
              Motivated Computer Science graduate with hands-on experience building AI-based applications, web
              prototypes and end-to-end CI/CD automation. Strong foundation in programming (Python), databases (MySQL,
              MongoDB), web technologies (HTML/CSS/JavaScript/React) and DevOps tooling (Docker, Jenkins, Kubernetes,
              ArgoCD, Terraform, Ansible).
            </p>

            <h4 className="mt-6 font-semibold">Soft skills</h4>
            <ul className="mt-2 list-disc list-inside text-slate-700">
              <li>Problem-solving</li>
              <li>Team collaboration & communication</li>
              <li>Time management & adaptability</li>
            </ul>
          </div>

          <aside className="bg-white rounded-2xl p-6 shadow-sm">
            <h4 className="font-semibold">Technical Skills</h4>
            <div className="mt-3 text-sm text-slate-700 space-y-2">
              <div>
                <strong>Languages:</strong> Python, JavaScript, HTML, CSS
              </div>
              <div>
                <strong>Web / Frameworks:</strong> ReactJS
              </div>
              <div>
                <strong>Databases:</strong> MySQL, MongoDB
              </div>
              <div>
                <strong>DevOps / Cloud:</strong> Docker, Jenkins, Kubernetes, ArgoCD, Terraform, Ansible, AWS EC2
              </div>
              <div>
                <strong>Tools:</strong> VS Code, Jupyter Notebook
              </div>
            </div>
          </aside>
        </section>

        {/* Projects */}
        <section id="projects" className="mb-8">
          <h3 className="text-xl font-semibold mb-4">Selected Projects</h3>
          <div className="grid md:grid-cols-3 gap-6">
            <article className="bg-white p-5 rounded-2xl shadow-sm">
              <h4 className="font-bold">AI Fitness Trainee</h4>
              <p className="mt-2 text-sm text-slate-700">
                Developed an AI-based fitness trainer using Python, OpenCV, and MediaPipe for real-time human pose
                detection and exercise tracking. Supports squats, push-ups and bicep curls by analysing body landmarks
                and angles. Live camera overlay displays pose skeletons and performance indicators.
              </p>
              <div className="mt-4 flex justify-between items-center">
                <a
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                  className="text-sm hover:underline"
                >
                  View code
                </a>
                <span className="text-xs text-slate-500">Python • OpenCV • MediaPipe</span>
              </div>
            </article>

            <article className="bg-white p-5 rounded-2xl shadow-sm">
              <h4 className="font-bold">Course Navigator</h4>
              <p className="mt-2 text-sm text-slate-700">
                Personalised course recommendation system using machine learning and user data to tailor course
                suggestions according to preferences and career goals, helping learners discover relevant courses.
              </p>
              <div className="mt-4 flex justify-between items-center">
                <a
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                  className="text-sm hover:underline"
                >
                  View code
                </a>
                <span className="text-xs text-slate-500">ML • Python • Recommendations</span>
              </div>
            </article>

            <article className="bg-white p-5 rounded-2xl shadow-sm">
              <h4 className="font-bold">CI/CD Pipeline Implementation</h4>
              <p className="mt-2 text-sm text-slate-700">
                Designed and implemented CI/CD pipeline using EC2, Jenkins, Docker, Kubernetes, ArgoCD and GitHub.
                Containerised applications and deployed to a Kubernetes cluster with GitOps for continuous delivery,
                improving deployment speed and reliability.
              </p>
              <div className="mt-4 flex justify-between items-center">
                <a
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                  className="text-sm hover:underline"
                >
                  View code
                </a>
                <span className="text-xs text-slate-500">DevOps • Jenkins • Kubernetes • ArgoCD</span>
              </div>
            </article>
          </div>
        </section>

        {/* Education + Certificates */}
        <section id="education" className="grid md:grid-cols-2 gap-6 mb-8">
          <div className="bg-white p-6 rounded-2xl shadow-sm">
            <h4 className="font-semibold">Education</h4>
            <ul className="mt-3 space-y-3 text-sm text-slate-700">
              <li>
                <strong>B.Tech — Computer Science Engineering</strong>
                <div>Rajiv Gandhi University of Knowledge Technologies | A.P • 2021—2025 • CGPA: 8.8</div>
              </li>
              <li>
                <strong>Pre-University Course</strong>
                <div>Rajiv Gandhi University of Knowledge Technologies | A.P • 2019—2021 • CGPA: 9.8</div>
              </li>
              <li>
                <strong>Secondary School Certificate (SSC)</strong>
                <div>Alpha High School | A.P • 2018—2019 • CGPA: 10.0</div>
              </li>
            </ul>
          </div>

          <div className="bg-white p-6 rounded-2xl shadow-sm">
            <h4 className="font-semibold">Certificates</h4>
            <ul className="mt-3 space-y-2 text-sm text-slate-700">
              <li>Domain: Cloud Computing • NPTEL</li>
              <li>Machine Learning • Coincent (Course Completion)</li>
              <li>Soft Skills • Tata Consultancy Services (Course Completion)</li>
            </ul>
          </div>
        </section>

        {/* Languages + Declaration */}
        <section className="grid md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-2xl shadow-sm">
            <h4 className="font-semibold">Languages</h4>
            <ul className="mt-3 text-sm text-slate-700">
              <li>English — Fluent</li>
              <li>Telugu — Native</li>
              <li>Hindi — Proficient</li>
            </ul>
          </div>

          <div className="md:col-span-2 bg-white p-6 rounded-2xl shadow-sm">
            <h4 className="font-semibold">Declaration</h4>
            <p className="mt-3 text-sm text-slate-700">I hereby declare that the above particulars and information stated are true, correct and complete to the best of my belief and knowledge.</p>
          </div>
        </section>

        {/* Contact */}
        <section id="contact" className="bg-white p-6 rounded-2xl shadow-sm">
          <h3 className="text-lg font-semibold">Contact</h3>
          <div className="mt-4 md:flex md:items-center md:justify-between gap-6">
            <div className="space-y-1 text-sm">
              <p>
                Email: <a className="font-medium" href="mailto:pushpashreebellamkonda@gmail.com">pushpashreebellamkonda@gmail.com</a>
              </p>
              <p>
                Phone: <span className="font-medium">+91 9177394740</span>
              </p>
              <p>
                GitHub: <a className="font-medium" href="https://github.com/PushpaShreeBellamkonda" target="_blank" rel="noreferrer">github.com/PushpaShreeBellamkonda</a>
              </p>
              <p>
                LinkedIn: <a className="font-medium" href="https://www.linkedin.com/in/bellamkonda-pushpa-shree-916a89248" target="_blank" rel="noreferrer">linkedin.com/in/bellamkonda-pushpa-shree-916a89248</a>
              </p>
            </div>

            <div className="mt-4 md:mt-0 flex flex-col sm:flex-row gap-3">
              <a
                href="/PushpaShreeBellamkonda.pdf"
                className="inline-block rounded-full border px-5 py-2 text-sm text-center hover:bg-slate-50"
              >
                Download Resume (PDF)
              </a>
              <a
                href="https://github.com/PushpaShreeBellamkonda"
                target="_blank"
                rel="noreferrer"
                className="inline-block rounded-full border px-5 py-2 text-sm text-center hover:bg-slate-50"
              >
                View Projects on GitHub
              </a>
            </div>
          </div>
        </section>

        <footer className="mt-10 text-center text-xs text-slate-500">© {new Date().getFullYear()} Bellamkonda Pushpa Shree — Built with ❤️</footer>
      </main>
    </div>
  );
}
