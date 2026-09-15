(function () {
  const drawer = document.querySelector("[data-drawer]");
  const openBtn = document.querySelector("[data-drawer-open]");
  const closeEls = document.querySelectorAll("[data-drawer-close]");

  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("is-open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }

  openBtn?.addEventListener("click", () => setDrawer(true));
  closeEls.forEach((el) => el.addEventListener("click", () => setDrawer(false)));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setDrawer(false);
  });
})();
