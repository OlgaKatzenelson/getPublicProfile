
$("#profile-info").hide();
$("#error").hide();

$('#search-form').on('submit', function(event){
    event.preventDefault();
    getProfile();
});


function getProfile() {
    $.ajax({
        url : "/getProfile", // the endpoint
        type : "POST",
        data : { url : $('#url-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            if (json.hasOwnProperty('data')){
                profile = $.parseJSON(json.data)[0].fields
                $('#name').text(profile.name)
                $('#title').text(profile.title)
                $('#current_position').text(profile.current_position)
                $('#summary').text(profile.summary)
                $('#skills').text(profile.skills)

                $("#error").hide();
                $('#profile-info').show()

                $.ajax({
                    url : "/getNumberOfTopSkills", // the endpoint
                    type : "POST",
                    data : { url : $('#url-text').val() }, // data sent with the post request

                    // handle a successful response
                    success : function(json) {
                        $('#url-text').val(''); // remove the value from the input
                        if (json.hasOwnProperty('data')){
                            $('#count_top_skills').text(json.data)
                        }else if(json.hasOwnProperty('error')){
                            $('#error').html("<div class='isa_error'><i class='fa fa-times-circle'></i> Error: " + json.error + "</div>")
                            $("#profile-info").hide();
                            $('#error').show()
                        }


                        console.log("success"); // another sanity check
                    },

                    // handle a non-successful response
                    error : errorFunction
                });

            }else if(json.hasOwnProperty('error')){
                $('#error').html("<div class='isa_error'><i class='fa fa-times-circle'></i> Error: " + json.error + "</div>")
                $("#profile-info").hide();
                $('#error').show()
            }


            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : errorFunction
    });

    function errorFunction(xhr,errmsg,err) {
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }

};
