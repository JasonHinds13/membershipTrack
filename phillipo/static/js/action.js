
//control nav bar navigations
function navigate(navId){

  if(navId == "home"){
    location.href="/"
  }

  else if (navId == "mems"){
    location.href="/members"
  }

  else if (navId == "search"){
    location.href="/search"
  }

  else if (navId == "admin"){
    location.href="/admin"
  }
}

//handles queries
function search()
{
  var lookup = document.getElementById("query").value;
  alert("Not Yet Implemented");
}
