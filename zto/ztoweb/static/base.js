const NAVBAR_CONTENT_HIDDEN_CLASS = "navbar-wrapped";
const NAVBAR_CONTENT_VISIBLE_CLASS = "navbar-unwrapped";
const NAVBAR_PLAY_NARROW_ANIM_CLASS = "navbar-play-narrow-anim";
const NAVBAR_PLAY_WIDEN_ANIM_CLASS = "navbar-play-widen-anim";
const NAVBAR_ID = "navbar";

function navbarToggle() {
  const navbar = document.getElementById(NAVBAR_ID);

  if (navbar.classList.contains(NAVBAR_CONTENT_HIDDEN_CLASS)) {
    navbar.classList.remove(NAVBAR_CONTENT_HIDDEN_CLASS);
    navbar.classList.add(NAVBAR_CONTENT_VISIBLE_CLASS);

    navbar.classList.remove(NAVBAR_PLAY_NARROW_ANIM_CLASS);
    navbar.classList.add(NAVBAR_PLAY_WIDEN_ANIM_CLASS);
  } else {
    navbar.classList.remove(NAVBAR_CONTENT_VISIBLE_CLASS);
    navbar.classList.add(NAVBAR_CONTENT_HIDDEN_CLASS);

    navbar.classList.remove(NAVBAR_PLAY_WIDEN_ANIM_CLASS);
    navbar.classList.add(NAVBAR_PLAY_NARROW_ANIM_CLASS);
  }
}
