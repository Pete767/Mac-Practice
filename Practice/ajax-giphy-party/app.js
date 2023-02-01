console.log("Let's get this party started!");
const $gifArea = $("#gif-area");
const $searchInput = $("#search");

function addGif(res){
    let totalResults = res.data.length;
    if (totalResults){
        let ranResult = Math.floor(Math.random() * totalResults);
        let $newCol = $("<div>", { class: "col-md-4 col-12 mb-4" });
        let $newGif = $("<img>", {
            src: res.data[ranResult].images.original.url,
            class: "w-100"
        });
        $newCol.append($newGif);
    $gifArea.append($newCol);
    }
}

$("form").on("submit", async function(evt) {
    evt.preventDefault();
  
    let searchTerm = $searchInput.val();
    $searchInput.val("");
  
    const response = await axios.get("http://api.giphy.com/v1/gifs/search", {
      params: {
        q: searchTerm,
        api_key: "MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym"
      }
    });
    addGif(response.data);
  });

  $("#remove").on("click", function() {
    $gifArea.empty();
  });