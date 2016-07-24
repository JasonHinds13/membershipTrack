
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
  location.href="/search/"+lookup;
}

//handles view by month
function navmonth(monthId)
{
  location.href="/members/"+monthId;
}