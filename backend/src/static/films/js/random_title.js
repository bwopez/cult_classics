function get_random(items) {
    return items[Math.floor(Math.random()*items.length)];
}

function display_random() {
    let titles_on_page = document.getElementsByClassName("titles");
    let random_title = get_random(titles_on_page);
    // set an area for the title to be rendered in
}