/** GreenCheck Theme **/

document.addEventListener("DOMContentLoaded", function () {

    const menuButton = document.querySelector(
        ".greencheck-menu-toggle"
    );

    const navigation = document.querySelector(
        ".greencheck-navigation"
    );

    if (!menuButton || !navigation) {
        return;
    }


    /* =====================================================
       Ouverture / fermeture du menu mobile
       ===================================================== */

    menuButton.addEventListener("click", function () {

        const isOpen = navigation.classList.toggle(
            "is-open"
        );

        menuButton.classList.toggle(
            "is-open",
            isOpen
        );

        menuButton.setAttribute(
            "aria-expanded",
            isOpen ? "true" : "false"
        );

        menuButton.setAttribute(
            "aria-label",
            isOpen
                ? "Fermer le menu"
                : "Ouvrir le menu"
        );
    });


    /* =====================================================
       Fermeture après clic sur un lien
       ===================================================== */

    const menuLinks = navigation.querySelectorAll(
        ".greencheck-nav-link"
    );

    menuLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navigation.classList.remove(
                "is-open"
            );

            menuButton.classList.remove(
                "is-open"
            );

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Ouvrir le menu"
            );
        });

    });


    /* =====================================================
       Fermeture avec la touche Échap
       ===================================================== */

    document.addEventListener("keydown", function (event) {

        if (
            event.key === "Escape" &&
            navigation.classList.contains("is-open")
        ) {

            navigation.classList.remove(
                "is-open"
            );

            menuButton.classList.remove(
                "is-open"
            );

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Ouvrir le menu"
            );
        }

    });

});