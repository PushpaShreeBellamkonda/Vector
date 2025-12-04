import React from "react";
import { motion } from "framer-motion";

export default function PushpaShreePortfolio() {
  const fadeUp = {
    hidden: { opacity: 0, y: 24 },
    visible: { opacity: 1, y: 0 },
  };

  const fadeIn = {
    hidden: { opacity: 0 },
    visible: { opacity: 1 },
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 relative overflow-hidden">
      {/* Brighter background blobs + subtle grid */}
      <div className="pointer-events-none fixed inset-0 -z-20">
        <div className="absolute inset-0 opacity-[0.4] bg-[radial-gradient(circle_at_1px_1px,#e2e8f0_1px,transparent_0)] [background-size:18px_18px]" />
        <div className="absolute -top-40 -left-10 h-80 w-80 rounded-full bg-sky-200/80 blur-3xl" />
        <div className="absolute -top-20 right-0 h-72 w-72 rounded-full bg-indigo-200/80 blur-3xl" />
        <div className="absolute bottom-[-80px] left-10 h-72 w-72 rounded-full bg-emerald-200/80 blur-3xl" />
        <div className="absolute bottom-[-60px] right-[-40px] h-72 w-72 rounded-full bg-slate-200/80 blur-3xl" />
      </div>

      {/* HEADER */}
      <header className="max-w-6xl mx-auto px-4 sm:px-6 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 relative z-10">
        <motion.div
          className="flex items-center gap-4"
          initial="hidden"
          animate="visible"
          variants={fadeUp}
          transition={{ duration: 0.4 }}
        >
          <div className="relative">
            {/* Softer colorful ring */}
            <div className="absolute -inset-1 rounded-full bg-[conic-gradient(from_180deg_at_50%_50%,#38bdf8,#6366f1,#22c55e,#f97316,#38bdf8)] opacity-70 blur" />
            <div className="relative w-16 h-16 md:w-20 md:h-20 rounded-full bg-white border border-slate-200 flex items-center justify-center text-slate-800 font-bold text-xl md:text-2xl shadow-md shadow-sky-100">
              PB
            </div>
          </div>
          <div>
            <p className="inline-flex items-center gap-2 rounded-full bg-sky-50 border border-sky-200 px-3 py-1 text-[0.7rem] text-sky-700 mb-1">
              <span className="inline-block h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse" />
              Open to Software Developer / DevOps roles
            </p>
            <h1 className="text-2xl md:text-3xl font-extrabold tracking-tight">
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-600 via-indigo-600 to-emerald-600">
                Bellamkonda Pushpa Shree
              </span>
            </h1>
            <p className="text-xs sm:text-sm text-slate-600 mt-1">
              B.Tech — Computer Science Engineering • CGPA: 8.8
            </p>
          </div>
        </motion.div>

        <motion.nav
          className="flex flex-wrap items-center gap-2 sm:gap-3 bg-white/80 border border-slate-200 rounded-full px-3 py-1.5 backdrop-blur-lg shadow-sm shadow-slate-200"
          initial="hidden"
          animate="visible"
          variants={fadeIn}
          transition={{ delay: 0.1, duration: 0.4 }}
        >
          {[
            ["About", "#about"],
            ["Projects", "#projects"],
            ["Skills", "#skills"],
            ["Education", "#education"],
            ["Contact", "#contact"],
          ].map(([label, href]) => (
            <a
              key={href}
              href={href}
              className="text-xs sm:text-sm px-3 py-1 rounded-full text-slate-700 hover:text-slate-900 hover:bg-sky-100 transition-colors"
            >
              {label}
            </a>
          ))}
        </motion.nav>
      </header>

      {/* MAIN */}
      <main className="max-w-6xl mx-auto px-4 sm:px-6 pb-16 pt-6 relative z-10">
        {/* HERO / ABOUT */}
        <motion.section
          id="about"
          className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-white via-sky-50 to-indigo-50 border border-slate-200 p-6 md:p-10 mb-10 shadow-[0_18px_40px_rgba(148,163,184,0.35)]"
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 0.4 }}
          variants={fadeUp}
          transition={{ duration: 0.5 }}
        >
          <div className="absolute inset-x-0 -top-40 h-64 bg-gradient-to-r from-sky-100 via-indigo-100 to-emerald-100 blur-3xl" />

          <div className="relative md:flex md:items-center md:justify-between gap-10">
            <div className="max-w-2xl">
              <p className="inline-flex items-center gap-2 rounded-full bg-white border border-indigo-200 px-3 py-1 text-xs font-medium text-indigo-700 mb-3">
                <span className="text-base">👋</span>
                <span>Hi, I&apos;m Pushpa — Mern stack Developer • DevOps • AI Enthusiast</span>
              </p>
              <h2 className="text-3xl md:text-4xl font-bold leading-tight text-slate-900">
                {" "}
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-sky-500 via-indigo-500 to-emerald-500">
                  About me
                </span>{" "}
                
              </h2>
              <p className="mt-4 text-sm sm:text-base text-slate-700 leading-relaxed">
                I&apos;m a Computer Science graduate passionate about software development, AI-based
                applications, and DevOps automation. I enjoy turning ideas into interactive, user-friendly and
                production-ready solutions using tools like Python , JavaScript , React, Docker, Jenkins, Kubernetes and
                cloud platforms.
              </p>

              <div className="mt-6 flex flex-wrap gap-3">
                <a
                  href="mailto:pushpashreebellamkonda@gmail.com"
                  className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-sky-500 to-indigo-500 px-5 py-2.5 text-sm font-medium text-white shadow-md shadow-sky-200 transition-transform hover:-translate-y-0.5"
                >
                  <span>📬</span> Contact Me
                </a>
                <a
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-2 rounded-full bg-white border border-sky-200 px-5 py-2.5 text-sm text-sky-700 hover:bg-sky-50 transition-transform hover:-translate-y-0.5"
                >
                  <span>💻</span> GitHub
                </a>
                <a
                  href="https://www.linkedin.com/in/bellamkonda-pushpa-shree-916a89248"
                  target="_blank"
                  rel="noreferrer"
                  className="inline-flex items-center gap-2 rounded-full bg-white border border-emerald-200 px-5 py-2.5 text-sm text-emerald-700 hover:bg-emerald-50 transition-transform hover:-translate-y-0.5"
                >
                  <span>🌐</span> LinkedIn
                </a>
              </div>

              <div className="mt-6 flex flex-wrap gap-2 text-[0.7rem] uppercase tracking-[0.22em]">
                {[
                  { label: "AI & Computer Vision", color: "from-sky-100 to-sky-50", text: "text-sky-700" },
                  { label: "Web Development", color: "from-indigo-100 to-indigo-50", text: "text-indigo-700" },
                  { label: "CI/CD & DevOps", color: "from-emerald-100 to-emerald-50", text: "text-emerald-700" },
                ].map((chip) => (
                  <span
                    key={chip.label}
                    className={`px-3 py-1 rounded-full border border-white/60 bg-gradient-to-r ${chip.color} text-[0.65rem] font-semibold ${chip.text}`}
                  >
                    {chip.label}
                  </span>
                ))}
              </div>
            </div>

            {/* Right card */}
            <motion.div
              className="mt-8 md:mt-0 md:self-stretch md:min-w-[260px]"
              initial={{ opacity: 0, x: 40 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, amount: 0.5 }}
              transition={{ duration: 0.5, delay: 0.1 }}
            >
              <div className="relative h-full">
                <div className="absolute inset-0 rounded-3xl bg-gradient-to-br from-sky-100 via-indigo-100 to-emerald-100 blur-2xl" />
                <div className="relative w-full md:w-64 lg:w-72 rounded-3xl border border-slate-200 bg-white/95 p-5 shadow-md shadow-slate-200">
                  <p className="text-xs uppercase tracking-[0.25em] text-slate-500 mb-4">
                    Quick Snapshot
                  </p>
                  <dl className="space-y-3 text-sm">
                    <div>
                      <dt className="text-slate-500">Role</dt>
                      <dd className="font-medium text-sky-700">
                        Software Developer / DevOps Enthusiast
                      </dd>
                    </div>
                    <div>
                      <dt className="text-slate-500">Location</dt>
                      <dd className="font-medium text-indigo-700">India , Hyderabad , Telangana</dd>
                    </div>
                    <div>
                      <dt className="text-slate-500">Strengths</dt>
                      <dd className="text-slate-700">
                        Problem solving • Learning fast • Team collaboration
                      </dd>
                    </div>
                    <div>
                      <dt className="text-slate-500">Interests</dt>
                      <dd className="text-slate-700">
                        AI, Web Apps, CI/CD, Cloud, Automation
                      </dd>
                    </div>
                  </dl>
                </div>
              </div>
            </motion.div>
          </div>
        </motion.section>

        {/* SKILLS + PROFILE */}
        <section
          id="skills"
          className="grid md:grid-cols-[minmax(0,2fr)_minmax(0,1.2fr)] gap-6 mb-10"
        >
          {/* Profile */}
          <motion.div
            className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
            transition={{ duration: 0.45 }}
          >
            <h3 className="text-lg font-semibold flex items-center gap-2 text-slate-900">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-sky-100 text-sky-600 text-sm">
                👩‍💻
              </span>
              Profile
            </h3>
            <p className="mt-3 text-sm sm:text-base text-slate-700 leading-relaxed">
              Motivated Computer Science graduate with experience building AI-based applications, web
              projects, and CI/CD pipelines. I work with Python, JavaScript, React, SQL/NoSQL databases, and
              DevOps tools to deliver robust, maintainable solutions. I enjoy collaborating with teams,
              communicating clearly, and continuously improving my technical and soft skills.
            </p>

            <h4 className="mt-6 font-semibold text-slate-900">Soft Skills</h4>
            <div className="mt-3 flex flex-wrap gap-2">
              {[
                { label: "Problem-solving", color: "from-sky-100 to-sky-50", text: "text-sky-700" },
                { label: "Team collaboration", color: "from-indigo-100 to-indigo-50", text: "text-indigo-700" },
                { label: "Communication", color: "from-emerald-100 to-emerald-50", text: "text-emerald-700" },
                { label: "Time management", color: "from-amber-100 to-amber-50", text: "text-amber-700" },
                { label: "Adaptability", color: "from-slate-100 to-slate-50", text: "text-slate-700" },
              ].map((chip) => (
                <span
                  key={chip.label}
                  className={`inline-flex items-center rounded-full bg-gradient-to-r ${chip.color} px-3 py-1 text-xs font-medium ${chip.text} border border-white`}
                >
                  {chip.label}
                </span>
              ))}
            </div>
          </motion.div>

          {/* Technical Skills */}
          <motion.aside
            className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
            transition={{ duration: 0.45, delay: 0.05 }}
          >
            <h4 className="font-semibold text-slate-900 flex items-center gap-2">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-emerald-100 text-emerald-600 text-sm">
                ⚙️
              </span>
              Technical Skills
            </h4>
            <div className="mt-4 space-y-3 text-xs sm:text-sm text-slate-700">
              <div>
                <p className="text-slate-500 text-[0.7rem] uppercase tracking-[0.18em] mb-1">
                  Languages
                </p>
                <p>Python, JavaScript, HTML, CSS</p>
              </div>
              <div>
                <p className="text-slate-500 text-[0.7rem] uppercase tracking-[0.18em] mb-1">
                  Web / Frameworks
                </p>
                <p>ReactJS</p>
              </div>
              <div>
                <p className="text-slate-500 text-[0.7rem] uppercase tracking-[0.18em] mb-1">
                  Databases
                </p>
                <p>MySQL, MongoDB</p>
              </div>
              <div>
                <p className="text-slate-500 text-[0.7rem] uppercase tracking-[0.18em] mb-1">
                  DevOps / Cloud
                </p>
                <p>Docker, Jenkins, Kubernetes, ArgoCD, Terraform, Ansible, AWS EC2</p>
              </div>
              <div>
                <p className="text-slate-500 text-[0.7rem] uppercase tracking-[0.18em] mb-1">
                  Tools
                </p>
                <p>VS Code, Jupyter Notebook</p>
              </div>
            </div>
          </motion.aside>
        </section>

        {/* PROJECTS */}
        <section id="projects" className="mb-10">
          <motion.h3
            className="text-xl font-semibold mb-4 flex items-center gap-2 text-slate-900"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.2 }}
            variants={fadeUp}
          >
            <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-amber-100 text-amber-600 text-sm">
              🚀
            </span>
            Selected Projects
          </motion.h3>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              {
                title: "AI Fitness Trainee",
                desc: "AI-based fitness trainer using Python, OpenCV, and MediaPipe for real-time pose detection and exercise tracking with live camera overlays.",
                tech: "Python • OpenCV • MediaPipe",
                border: "from-sky-200 via-sky-100 to-white",
              },
              {
                title: "Course Navigator",
                desc: "Personalised course recommendation system that suggests courses aligned with user preferences and career goals using basic ML techniques.",
                tech: "Machine Learning • Python",
                border: "from-indigo-200 via-indigo-100 to-white",
              },
              {
                title: "CI/CD Pipeline Implementation",
                desc: "End-to-end CI/CD pipeline on AWS EC2 using Jenkins, Docker, Kubernetes and ArgoCD to automate build, test and deployment workflows.",
                tech: "DevOps • Jenkins • Kubernetes • ArgoCD",
                border: "from-emerald-200 via-emerald-100 to-white",
              },
            ].map((project, index) => (
              <motion.article
                key={project.title}
                className="group relative"
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true, amount: 0.3 }}
                variants={fadeUp}
                transition={{ duration: 0.45, delay: 0.05 * index }}
              >
                {/* Light color border wrapper */}
                <div
                  className={`absolute -inset-[1px] rounded-2xl bg-gradient-to-br ${project.border} opacity-80 group-hover:opacity-100 blur-[1px] transition-opacity duration-300`}
                />
                <div className="relative overflow-hidden rounded-2xl bg-white/95 border border-slate-200 p-5 shadow-md shadow-slate-200 transition-transform duration-300 group-hover:-translate-y-1">
                  <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-gradient-to-br from-white/60 via-transparent to-white/60" />
                  <div className="relative">
                    <h4 className="font-semibold text-base sm:text-lg text-slate-900">
                      {project.title}
                    </h4>
                    <p className="mt-2 text-xs sm:text-sm text-slate-700 leading-relaxed min-h-[72px]">
                      {project.desc}
                    </p>
                    <div className="mt-4 flex items-center justify-between gap-3">
                      <a
                        href="https://github.com/PushpaShreeBellamkonda"
                        target="_blank"
                        rel="noreferrer"
                        className="text-xs sm:text-sm inline-flex items-center gap-1 text-sky-700 hover:text-sky-900"
                      >
                        View code <span className="text-base leading-none">↗</span>
                      </a>
                      <span className="text-[0.7rem] text-right text-slate-500">
                        {project.tech}
                      </span>
                    </div>
                  </div>
                </div>
              </motion.article>
            ))}
          </div>
        </section>

        {/* EDUCATION + CERTIFICATES */}
        <section id="education" className="grid md:grid-cols-2 gap-6 mb-10">
          <motion.div
            className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
          >
            <h4 className="font-semibold text-slate-900 flex items-center gap-2">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-indigo-100 text-indigo-600 text-sm">
                🎓
              </span>
              Education
            </h4>
            <ul className="mt-4 space-y-4 text-xs sm:text-sm text-slate-700">
              <li>
                <p className="font-semibold text-sky-700">
                  B.Tech — Computer Science Engineering
                </p>
                <p>Rajiv Gandhi University of Knowledge Technologies, A.P (2021–2025)</p>
                <p className="text-slate-500">CGPA: 8.8</p>
              </li>
              <li>
                <p className="font-semibold text-indigo-700">Pre-University Course</p>
                <p>Rajiv Gandhi University of Knowledge Technologies, A.P (2019–2021)</p>
                <p className="text-slate-500">CGPA: 9.8</p>
              </li>
              <li>
                <p className="font-semibold text-emerald-700">Secondary School Certificate (SSC)</p>
                <p>Alpha High School, A.P (2018–2019)</p>
                <p className="text-slate-500">CGPA: 10.0</p>
              </li>
            </ul>
          </motion.div>

          <motion.div
            className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
            transition={{ delay: 0.05 }}
          >
            <h4 className="font-semibold text-slate-900 flex items-center gap-2">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-amber-100 text-amber-600 text-sm">
                📜
              </span>
              Certificates
            </h4>
            <ul className="mt-4 space-y-3 text-xs sm:text-sm text-slate-700">
              <li>Cloud Computing — NPTEL</li>
              <li>Machine Learning — Coincent (Course Completion)</li>
              <li>Soft Skills — Tata Consultancy Services (Course Completion)</li>
            </ul>
          </motion.div>
        </section>

        {/* LANGUAGES + DECLARATION */}
        <section className="grid md:grid-cols-3 gap-6 mb-10">
          <motion.div
            className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
          >
            <h4 className="font-semibold text-slate-900 flex items-center gap-2">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-emerald-100 text-emerald-600 text-sm">
                🌐
              </span>
              Languages
            </h4>
            <ul className="mt-4 space-y-2 text-xs sm:text-sm text-slate-700">
              <li>English — Fluent</li>
              <li>Telugu — Native</li>
              <li>Hindi — Proficient</li>
            </ul>
          </motion.div>

          <motion.div
            className="md:col-span-2 rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
            transition={{ delay: 0.05 }}
          >
            <h4 className="font-semibold text-slate-900 flex items-center gap-2">
              <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-slate-100 text-slate-700 text-sm">
                ✍️
              </span>
              Declaration
            </h4>
            <p className="mt-3 text-xs sm:text-sm text-slate-700 leading-relaxed">
              I hereby declare that the above particulars and information stated are true, correct and
              complete to the best of my belief and knowledge.
            </p>
          </motion.div>
        </section>

        {/* CONTACT */}
        <section
          id="contact"
          className="rounded-2xl border border-slate-200 bg-white/95 p-6 shadow-md shadow-slate-200"
        >
          <motion.h3
            className="text-lg font-semibold flex items-center gap-2 text-slate-900"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
          >
            <span className="inline-flex h-7 w-7 items-center justify-center rounded-full bg-sky-100 text-sky-600 text-sm">
              📫
            </span>
            Contact
          </motion.h3>
          <motion.div
            className="mt-4 md:flex md:items-center md:justify-between gap-6"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: 0.3 }}
            variants={fadeUp}
            transition={{ delay: 0.05 }}
          >
            <div className="space-y-1 text-xs sm:text-sm text-slate-700">
              <p>
                Email:{" "}
                <a
                  className="font-medium text-sky-700 hover:text-sky-900"
                  href="mailto:pushpashreebellamkonda@gmail.com"
                >
                  pushpashreebellamkonda@gmail.com
                </a>
              </p>
              <p>
                Phone: <span className="font-medium text-emerald-700">+91 9177394740</span>
              </p>
              <p>
                GitHub:{" "}
                <a
                  className="font-medium text-indigo-700 hover:text-indigo-900"
                  href="https://github.com/PushpaShreeBellamkonda"
                  target="_blank"
                  rel="noreferrer"
                >
                  github.com/PushpaShreeBellamkonda
                </a>
              </p>
              <p>
                LinkedIn:{" "}
                <a
                  className="font-medium text-sky-700 hover:text-sky-900"
                  href="https://www.linkedin.com/in/bellamkonda-pushpa-shree-916a89248"
                  target="_blank"
                  rel="noreferrer"
                >
                  linkedin.com/in/bellamkonda-pushpa-shree-916a89248
                </a>
              </p>
            </div>

            <div className="mt-4 md:mt-0 flex flex-col sm:flex-row gap-3">
              {/* <a
                href="/PushpaShreeBellamkonda.pdf"
                className="inline-block rounded-full bg-slate-50 border border-slate-300 px-5 py-2 text-xs sm:text-sm text-center text-slate-800 hover:bg-slate-100 transition-transform hover:-translate-y-0.5"
              >
                Download Resume (PDF)
              </a> */}
              <a
                href="https://github.com/PushpaShreeBellamkonda"
                target="_blank"
                rel="noreferrer"
                className="inline-block rounded-full bg-gradient-to-r from-sky-500 to-indigo-500 px-5 py-2 text-xs sm:text-sm text-center font-medium text-white shadow-md shadow-sky-200 hover:shadow-sky-300 transition-transform hover:-translate-y-0.5"
              >
                View Projects on GitHub
              </a>
            </div>
          </motion.div>
        </section>

        <motion.footer
          className="mt-10 text-center text-[0.7rem] text-slate-500"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true, amount: 0.2 }}
          transition={{ duration: 0.6, delay: 0.1 }}
        >
          © {new Date().getFullYear()} Bellamkonda Pushpa Shree — Built with React & Tailwind
        </motion.footer>
      </main>
    </div>
  );
}
