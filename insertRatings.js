var professors = document.getElementsByClassName("SEC_FACULTY_INFO")
for (var i = 0; i < professors.length; i++){
	var dom = professors[i].getElementsByTagName("p");
	if (dom.length > 0){
		name = dom[0].innerHTML;
		if (name.startsWith("TBA") != true){
			requestRatings(name);
		}
	}
}

function requestRatings (name){
	var firstName = name.split(" ")[0];
	var lastName = name.split(" ")[1];
	console.log(firstName);
	console.log(lastName);
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "http://ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=University+of+Guelph&schoolID=1426&query=" + lastName, true);
	xhr.onreadystatechange = function(){
		if (xhr.readyState = 4){
			console.log(xhr.responseText);
		}
	};
	xhr.send(null);
	
}