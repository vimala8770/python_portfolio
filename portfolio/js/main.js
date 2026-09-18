document.addEventListener("DOMContentLoaded", () => {
    const nav = document.getElementById("siteNav");
    const backToTop = document.getElementById("backToTop");
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = [...document.querySelectorAll("section[id]")];

    const onScroll = () => {
        if (window.scrollY > 12) {
            nav.classList.add("shadow-sm");
        } else {
            nav.classList.remove("shadow-sm");
        }

        if (window.scrollY > 400) {
            backToTop.classList.add("is-visible");
        } else {
            backToTop.classList.remove("is-visible");
        }

        const current = sections.findLast((section) => window.scrollY >= section.offsetTop - 120);
        navLinks.forEach((link) => link.classList.remove("active"));
        if (current) {
            const active = document.querySelector(`.nav-link[href="#${current.id}"]`);
            if (active) {
                active.classList.add("active");
            }
        }
    };

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    backToTop.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    document.querySelectorAll('#primaryNav .nav-link, #primaryNav .btn-resume').forEach((link) => {
        link.addEventListener("click", () => {
            const collapse = document.getElementById("primaryNav");
            if (collapse.classList.contains("show")) {
                bootstrap.Collapse.getOrCreateInstance(collapse).hide();
            }
        });
    });
});
