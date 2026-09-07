const header = document.querySelector("[data-header]");
const menuButton = document.querySelector(".menu-button");
const navigation = document.querySelector(".site-nav");
const dialog = document.querySelector("[data-lightbox-dialog]");
const dialogImage = document.querySelector("[data-lightbox-image]");
const dialogCaption = document.querySelector("[data-lightbox-caption]");

const updateHeader = () => {
  header?.classList.toggle("is-scrolled", window.scrollY > 24);
};

updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

menuButton?.addEventListener("click", () => {
  const isOpen = menuButton.getAttribute("aria-expanded") === "true";
  menuButton.setAttribute("aria-expanded", String(!isOpen));
  navigation?.classList.toggle("is-open", !isOpen);
  menuButton.querySelector(".sr-only").textContent = isOpen ? "打开导航" : "关闭导航";
});

navigation?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    menuButton?.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
    menuButton.querySelector(".sr-only").textContent = "打开导航";
  });
});

document.querySelectorAll(".reveal").forEach((element) => {
  const delay = element.dataset.delay;
  if (delay) element.style.setProperty("--delay", `${delay}ms`);
});

if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.12 }
  );
  document.querySelectorAll(".reveal").forEach((element) => {
    element.classList.add("will-reveal");
    observer.observe(element);
  });
} else {
  document.querySelectorAll(".reveal").forEach((element) => element.classList.add("is-visible"));
}

const revealCurrentAnchor = () => {
  if (!window.location.hash) return;
  let anchor;
  try { anchor = decodeURIComponent(window.location.hash.slice(1)); } catch { return; }
  const target = document.getElementById(anchor);
  if (!target) return;
  if (target.classList.contains("reveal")) target.classList.add("is-visible");
  target.querySelectorAll(".reveal").forEach((element) => element.classList.add("is-visible"));
};

revealCurrentAnchor();
window.addEventListener("hashchange", revealCurrentAnchor);

document.querySelectorAll("[data-lightbox]").forEach((button) => {
  button.addEventListener("click", () => {
    if (!dialog || !dialogImage || !dialogCaption) return;
    dialogImage.src = button.dataset.lightbox;
    dialogImage.alt = button.dataset.caption || "实验结果图片";
    dialogCaption.textContent = button.dataset.caption || "";
    dialog.showModal();
  });
});

dialog?.querySelector(".lightbox-close")?.addEventListener("click", () => dialog.close());
dialog?.addEventListener("click", (event) => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && menuButton?.getAttribute("aria-expanded") === "true") {
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.querySelector(".sr-only").textContent = "打开导航";
    navigation?.classList.remove("is-open");
    menuButton.focus();
  }
});

document.querySelectorAll("[data-year]").forEach((element) => {
  element.textContent = String(new Date().getFullYear());
});
