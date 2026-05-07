async function menuOpenClose() {
    if (!$("#menu").is(":animated")) {
        if ($("#menu").is(":hidden")) {
            $("#menu").show("1000");
        } else {
            $("#menu").hide("1000");
        }
    }
}

async function toggleDiv(name) {
    if ($("#" + name + "Checkbox").is(":checked")) {
        $("#" + name).show();
        localStorage.setItem(name, 'true');
    } else {
        $("#" + name).hide();
        localStorage.setItem(name, 'false');
    }
}

async function toggleDarkMode() {
    if ($("#darkModeCheckbox").is(":checked")) {
        $("html").attr('data-theme', 'dark');
        localStorage.setItem('darkMode', 'true');
    } else {
        $("html").attr('data-theme', 'light');
        localStorage.setItem('darkMode', 'false');
    }
}
