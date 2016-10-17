window.onload = function(){

  if (location.pathname == "/"){
    var x = document.querySelector("#home");
    x.setAttribute("class","active");
  }
  else if(location.pathname == "/members/"){
    var x = document.querySelector("#mems");
    x.setAttribute("class","active");
  }
  else if(location.pathname == "/search/"){
    var x = document.querySelector("#search");
    x.setAttribute("class","active");
  }
  else if(location.pathname == "/register/"){
    var x = document.querySelector("#register");
    x.setAttribute("class","active");
  }
}
  //control nav bar navigations
  function navigate(navId){

    if(navId == "home"){
      location.href="/";
    }

    else if (navId == "mems"){
      location.href="/members";
    }

    else if (navId == "search"){
      location.href="/search";
    }

    else if (navId == "admin"){
      location.href="/admin";
    }
    else if(navId == "register"){
      location.href="/register";
    }
  }

  //handles queries
  function search()
  {
    var lookup = document.getElementById("query").value;
    var newlook = lookup.replace(" ", "_");
    location.href="/search/"+newlook;
  }

  //handles view by month
  function navmonth(monthId)
  {
    location.href="/members/"+monthId;
  }
