let random_number = Math.floor(Math.random() * 151);

$.ajax({
    url: "https://api.thecatapi.com/v1/images/search",
    data: { params: { limit:1, size:"full" } },
    type: "GET",
    beforeSend: function(xhr){xhr.setRequestHeader('x-api-key', '6d8bab16-4c07-495e-a135-0c40ab341d7d');},
    success: function(data) { 
        $('#cats_random').attr('src', data[0].url);
    }
 });