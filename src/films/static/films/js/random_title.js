let titles_on_page = document.getElementsByClassName("titles");

function get_random(items) {
    return items[Math.floor(Math.random()*items.length)];
}

function display_random() {
    let random_title = get_random(titles_on_page);
    document.getElementById("random_movie_heading").style.display = "block";
    document.getElementById("random_title").innerHTML = random_title.innerHTML;
}