//const current = document.getElementById("current");

const submittro = document.getElementById('submittro').addEventListener("click", currentEvent);

	
	
/* It starts here get user data*/
	
	function currentEvent(e) {
	  e.preventDefault();
	
	  const Email = document.getElementById("email").value;
	  const Mobile = document.getElementById("mobile").value;
	  const Dob = document.getElementById("dob").value;
	  const Bname = document.getElementById("bname").value;
	  
      ///
    	let _data = {
    	  name: Bname,
    	  dob: Dob,
    	  mobile:Mobile,
    	  email: Email,
    	  reqFor:'Astro',
    	};
    	
    	/*
    	for(const contents in _data){
            console.log(
                `this is the contents = ${contents}: ${_data[contents]}`
            );
                        
        }
    	*/
    //	window.location = `https://wa.me/+2348136767311?text=${Bname} ${Dob} //${Mobile} ${Email}`;
    
    	
    	
    	// Example POST method implementation: 
    	//https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    	
        async function postData(url = "", data = {}) {
            // Default options are marked with *
            const response = await fetch(url, {
                method: "POST", // *GET, POST, PUT, DELETE, etc.
                mode: "cors", // no-cors, *cors, same-origin
                cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
                credentials: "same-origin", // include, *same-origin, omit
                headers: {
                  "Content-Type": "application/json",
                  // 'Content-Type': 'application/x-www-form-urlencoded',
                },
                redirect: "follow", // manual, *follow, error
                referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                body: JSON.stringify(data), // body data type must match "Content-Type" header
            });
        return response.json(); // parses JSON response into native JavaScript objects
        }

        postData("https://bpm.pythonanywhere.com/res", _data).then((data) => {
                    //{'approach':py_means[py_num]['APPROACH'], 'advice':py_means[py_num]['ADVICE'], 'pina':curr_pina}
                    
                    document.getElementById("displayCard").innerHTML = `
                            <span class="padding-bottom--15">${data['approach']}</span>

                              <form id="stripe-login">
                
                                <div class="field padding-bottom--24">
                                  <label for="email">My advice would be to</label>
                                  ${data['advice']}
                                </div>
                
                
                              </form>
                    
                    `;
                    
                    document.getElementById("delete").innerHTML = '';
            }
        );

    
    }
	
	
	