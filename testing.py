#coding=utf-8

from bs4 import BeautifulSoup

html_doc = '''<html class=" js flexbox flexboxlegacy canvas canvastext no-touch geolocation hashchange history draganddrop rgba backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage applicationcache svg inlinesvg svgclippaths"><!--<![endif]--><head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="google-site-verification" content="F8gUuqzRvOrAlhaGyP7aAuMs_Se8zK-98Ai2sNsIZEo">
  	<meta name="google-site-verification" content="hk1NnSbYuDC0Sppgbf7YIT-VxUiRbOVRdtqA4AmkGzM">
  	<meta name="google-site-verification" content="CKMC_IwvKoVbX1U8x1A9yzKABsSlop6qxfuDzwfV7Qs"> <!--  relaunch qa -->
  	<meta name="google-site-verification" content="1D_3ZfAdMu4Tki8pFRj68YAqYot-paTOoDVzCTIJZZI"> <!--  relaunch rmp -->
    <link rel="stylesheet" href="/assets/application-2e80095dbebab45492ab75c1d07257e7.css">
    <script async="" type="text/javascript" src="http://www.googletagservices.com/tag/js/gpt.js"></script><script async="" src="//connect.facebook.net/en_US/fbds.js"></script><script src="/assets/libs/jquery-7f5fea5cae853e98f1d3f5d509216bd4.js" type="text/javascript"></script>
    <script src="/assets/libs/cookie-a754825244f3c1c61d82143b07a90a75.js" type="text/javascript"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
    
     	<meta name="robots" content="all">
   	
    <meta name="description" content="Rating and reviews for Professor Alex Smith  from University of Guelph Guelph, ON Canada.">
    <title>Alex Smith at University of Guelph - RateMyProfessors.com</title>
    <meta property="og:url" content="http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1981141">
    <meta property="og:title" content="Alex Smith at University of Guelph - RateMyProfessors.com">
	  <meta property="og:description" content="Check out the ratings and reviews for Alex Smith  from University of Guelph in Guelph, ON">
	  
	     <meta property="og:image" content="http://www.ratemyprofessors.com/assets/RMP_logo.png">
	  

	  <meta property="og:type" content="website">

    <link rel="icon" href="/images/favicon-16.png">
    <link rel="icon" sizes="32×32" href="/images/favicon-32.png">
    <link rel="apple-touch-icon" href="/images/favicon-57.png">
    <link rel="apple-touch-icon" sizes="48×48" href="/images/favicon-48.png">
    <link rel="apple-touch-icon" sizes="72×72" href="/images/favicon-72.png">
    <link rel="apple-touch-icon" sizes="114×114" href="/images/favicon-114.png">
    <link rel="apple-touch-icon" sizes="152×152" href="/images/favicon-152.png">
    <link rel="apple-touch-icon-precomposed" href="/images/favicon-196.png">
    <link rel="stylesheet" href="https://mtvstatic-a.akamaihd.net/site/rmp/0.0/bundles/responsive_css_head.php">
    <!--[if IE]><link rel="shortcut icon" href="/images/favicon-16.ico" /> <![endif]-->
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="/images/favicon-16.png">
    <script>(function() {
    var _fbq = window._fbq || (window._fbq = []);
    if (!_fbq.loaded)
    { var fbds = document.createElement('script'); fbds.async = true; fbds.src = '//connect.facebook.net/en_US/fbds.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(fbds, s); _fbq.loaded = true; }
    _fbq.push(['addPixelId', '331289063738687']);
    })();
    window._fbq = window._fbq || [];
    window._fbq.push(['track', 'PixelInitialized', {}]);
    </script>
    <noscript>&lt;img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=331289063738687&amp;ev=PixelInitialized" /&gt;</noscript>

    
    
    
    

  <style type="text/css">:root .rmp_leaderboard,
:root #placeholder728,
:root #mtvBlock,
:root #cr-qsb,
:root .leaderboard_ad,
:root .ad.super,
:root #ad728,
:root #ad-container
{display:none !important;}</style><style>img[src="//ad.doubleclick.net/ddm/ad/N378.150781.4704472308521/B5632202.123250790;abr=!ie4;abr=!ie5;sz=160x600;mtfIFPath=rich_media_gallery_public/doubleclick/;ord=1453479256870?"],
img[src="//ad.doubleclick.net/ddm/ad/N378.150781.4704472308521/B5632202.123250790;abr=!ie4;abr=!ie5;sz=160x600;mtfIFPath=rich_media_gallery_public/doubleclick/;ord=1453479263250?"]
{display:none !important;}</style><script type="text/javascript" src="//mtvn.demdex.net/event?d_stuff=1&amp;d_dst=1&amp;d_rtbd=json&amp;d_cts=1&amp;d_cb=aam_tnt_cb"></script><script type="text/javascript" src="http://b.scorecardresearch.com/beacon.js?c1=2&amp;c2=6036034&amp;c3=&amp;c4=http%253A%2F%2Fwww.ratemyprofessors.com%2FShowRatings.jsp%253Ftid%253D1981141&amp;c5=20000&amp;c6=&amp;c15="></script><script type="text/javascript" src="//mtvn.demdex.net/event?d_rtbd=json&amp;d_dst=1&amp;d_cts=1&amp;d_cb=btg.Demdex.response&amp;c_uuid=null&amp;c_visit=www.ratemyprofessors.com_visit"></script><script type="text/javascript" src="//mtvn.demdex.net/event?d_rtbd=json&amp;d_dst=1&amp;d_cts=1&amp;d_cb=btg.Demdex.response&amp;c_pageName=%2Fprofessors%2FAlex%20Smith%2F1981141&amp;c_ch=professors&amp;c_v49=professors&amp;c_heir2=%2Fprofessors%2FAlex%20Smith%2F1981141&amp;c_c2=Canada&amp;c_c3=Biology&amp;c_c5=ON&amp;c_c6=University%20of%20Guelph&amp;c_c7=Alex%20Smith&amp;c_c8=visitor&amp;c_c9=1426&amp;c_c10=1981141&amp;c_section=professors&amp;c_h2=professors%2FAlex%20Smith%2F1981141&amp;c_events=event16&amp;c_v67=EMPTY_1453479352931&amp;c_c41=New&amp;c_host=www.ratemyprofessors.com"></script><script src="http://partner.googleadservices.com/gpt/pubads_impl_79.js" async=""></script><script type="text/javascript" src="//mtvn.demdex.net/event?d_rtbd=json&amp;d_dst=1&amp;d_cts=1&amp;d_cb=btg.Demdex.response&amp;c_linkName=PROF%3ATags_Cancel&amp;c_linkType=o&amp;c_lnk=true&amp;c_referrer=http%3A%2F%2Fwww.ratemyprofessors.com%2FShowRatings.jsp%3Ftid%3D1981141&amp;c_host=www.ratemyprofessors.com"></script></head>
  <body class="show_professor">

    
    <!-- <div class="overlay"></div> -->
    <!--do not modify this script -->
    <div id="mobileNav" class="slide">
      <div class="mobile_nav_wrap">
        <div class="navItems">
          <ul class="menuNav">
            <!-- One Menu Item -->
            <li>
              <a href="/mobile/professor_search">
                <span class="icon icon-professor"></span>
                <span class="title">Professors</span>
                <span class="arrow"></span>
              </a>
            </li>
            <!-- One Menu Item -->

            <!-- One Menu Item -->
            <li>
              <a href="/mobile/school_search">
                <span class="icon icon-school"></span>
                <span class="title">Schools</span>
                <span class="arrow"></span>
              </a>
            </li>
            <!-- One Menu Item -->

            <!-- One Menu Item -->
            <li>
              <a href="/mobile/rate_search">
                <span class="icon icon-rate"></span>
                <span class="title">Rate</span>
                <span class="arrow"></span>
              </a>
            </li>
            <!-- One Menu Item -->

            <!-- One Menu Item -->
            <li>
              <a href="/mobile/blog">
                <span class="icon icon-blog"></span>
                <span class="title">Blog</span>
                <span class="arrow"></span>
              </a>
            </li>
            <!-- One Menu Item -->

            <!-- One Menu Item -->
			 <li id="mobilemyProfContainer" class="hide">
                  <a href="/mobile/myprofs">
                    <span class="icon icon-my-profs"></span>
                    <span class="title">My Profs</span>
                    <span class="arrow"></span>
                  </a>
             </li>
             <script type="text/template" id="my-professor-result-template">
  				<li id = "my-professor-{{id}}">
   				 <a href="/ShowRatings.jsp?tid={{id}}&showMyProfs=true">
  			    <span class="{{ratingclass}}-icon"></span>
 			     <span class="remove-this-button" data-id="{{id}}">&#215;</span>
 			     <span class="rating">{{overall_rating}}</span>
 			     <span class="name">{{plname}}, {{{pfname}}}
  			      <span class="info">{{rating_count}} RATINGS</span>
  			    </span>
 			   </a>
 			 </li>
			</script>
            <!-- One Menu Item -->

            <!-- Not Logged In -->
            <div id="mobileLoginSectionContainer">
              
  <!-- Need ajax widget -->
  <li class="mobile_login logged_off">
    <a href="/member">
      <span class="mobile_login_text">log In</span>
      <span class="arrow"></span>
    </a>
  </li>


            </div>
            <li id="mobileSocial">
              <ul>
                <li><a href="https://www.facebook.com/RateMyProfessor" class="icon-facebook" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:facebook', linkType:'o' } );"></a></li>
                <li><a href="https://twitter.com/ratemyprofessor" class="icon-twitter" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:twitter', linkType:'o' } );"></a></li>
                <li><a href="http://ratemyprofessors.tumblr.com/" class="icon-tumblr" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:tumblr', linkType:'o' } );"></a></li>
                <li><a href="http://www.pinterest.com/ratemyprofessor/" class="icon-pinterest" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:pinterest', linkType:'o' } );"></a></li>
                <li><a href="http://instagram.com/ratemyprofessors" class="icon-instagram" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:instagram', linkType:'o' } );"></a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!-- Starts The Page Wrap -->
    <div id="container">
      <div class="overlay"></div>
      <!-- Begins Mobile Header -->
      <div id="mobileHeader" class="slide">
        <a id="mobileHamburger" href="#"><span></span></a>
        <a href="/" id="mLogo"></a>
        <a href="#" class="icon-search"></a>
        <div class="mobileSearch">
	        <div id="mSearchBox">
    	      <form class="main-search-form" action="/search.jsp"><input type="search" id="msearchr" name="query" placeholder="Search ..." class="ui-autocomplete-input" autocomplete="off"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span></form>
        	</div>
          <div id="headerAutocomplete" style="display: none;">
            <div class="results-container">
              <div id="header-results">
                <div class="professor-list">
                  <div class="label">Professors</div>
                  <ul></ul>
                  <a href="/search.jsp?queryBy=teacherName&amp;query={{requestparam}}" class="view-all view-all-professors">View All Professors</a>
                </div>
                <div class="school-list">
                  <div class="label">Schools</div>
                  <ul></ul>
                  <a href="/search.jsp?queryBy=schoolName&amp;query={{requestparam}}" class="view-all view-all-schools">View All Schools</a>
                </div>
              </div>
              <div id="header-no-results">
                Sorry No Results Found
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="mobileLeaderboardAd" class="top-header relative"><div id="mobileLeaderboardAdWrap"></div></div>
      <!-- Ends Mobile Header -->

      
        <section class="top-header relative">
  <div id="ad1x1" data-ad-sizes="1x1" data-ad-keyvalues="" data-ad-reload-interval="-1" style=""><div id="coda_ad_1x1_2" data-ad-sizes="1x1" data-ad-reload-interval="-1" style="position:absolute;visibility:hidden"></div></div>
  <div id="ad1x2" data-ad-sizes="1x2" data-ad-keyvalues="" data-ad-reload-interval="-1" style=""><div id="coda_ad_1x2_3" data-ad-sizes="1x2" data-ad-reload-interval="-1" style="position:absolute;visibility:hidden"></div></div>
  <div id="ad3x3" data-ad-sizes="3x3" data-ad-keyvalues="" data-ad-reload-interval="-1" style=""><div id="coda_ad_3x3_4" data-ad-sizes="3x3" data-ad-reload-interval="-1" style="position:absolute;visibility:hidden"></div></div>
  <div id="ad6x6" data-ad-sizes="6x6" data-ad-keyvalues="" data-ad-reload-interval="-1" style=""><div id="coda_ad_6x6_5" data-ad-sizes="6x6" data-ad-reload-interval="-1" style="position:absolute;visibility:hidden"></div></div>
  <article id="mtv_lead_1" class="ad leaderboard_ad">
  	<div id="ad728" style="text-align: center;"><div id="coda_ad_728x90_1" data-ad-sizes="728x90"></div></div>
  </article>
</section>


        <!-- Starts Header -->
        <header>
  <div class="overlay"></div>
  <a href="/" id="logo" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:Logo', linkType:'o' } );"></a>
  <!-- Starts the header search box -->
  <div id="searchBox">
    <div class="searchBox-wrapper">
      <form class="main-search-form" method="GET" action="/search.jsp"><input type="text" id="searchr" name="query" placeholder="Search for a professor or school" autocomplete="off" autocorrect="off" spellcheck="false" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'SEARCH:Filter', linkType:'o' } );" class="ui-autocomplete-input"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span></form>
      <div id="tablet-social-dropdown">
        <div class="tablet-social">
          <span class="social-text">Follow us</span>
        </div>
        <div class="tablet-social-list">
          <ul>
            <a href="https://www.facebook.com/RateMyProfessor" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:facebook', linkType:'o' } );">
              <li class="icon-facebook">
                <span class="text-social">facebook</span>
              </li>
            </a>
            <a href="https://twitter.com/ratemyprofessor" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:twitter', linkType:'o' } );">
              <li class="icon-twitter">
                <span class="text-social">twitter</span>
              </li>
            </a>
            <a href="http://ratemyprofessors.tumblr.com/" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:tumblr', linkType:'o' } );">
              <li class="icon-tumblr">
                <span class="text-social">tumblr</span>
              </li>
            </a>
            <a href="http://www.pinterest.com/ratemyprofessor/" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:pinterest', linkType:'o' } );">
              <li class="icon-pinterest">
                <span class="text-social">pinterest</span>
              </li>
            </a>
            <a href="http://instagram.com/ratemyprofessors" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:instagram', linkType:'o' } );">
              <li class="icon-instagram">
                <span class="text-social">instagram</span>
              </li>
            </a>
          </ul>
        </div>
      </div>
    </div>
    <div id="headerAutocomplete" style="display: none;">
      <div class="results-container">
        <div id="header-results">
          <div class="professor-list">
            <div class="label">Professors</div>
            <ul></ul>
            <a href="/search.jsp?queryBy=teacherName&amp;query={{requestparam}}" class="view-all view-all-professors">View All Professors</a>
          </div>
          <div class="school-list">
            <div class="label">Schools</div>
            <ul></ul>
            <a href="/search.jsp?queryBy=schoolName&amp;query={{requestparam}}" class="view-all view-all-schools">View All Schools</a>
          </div>
        </div>
        <div id="header-no-results">
          Sorry No Results Found
        </div>
      </div>
    </div>
  </div>
  <!-- Ends the header search box -->

  <!-- Starts the Head Social Bar -->
  <div id="headSocial">
    <ul>
      <li><a href="https://www.facebook.com/RateMyProfessor" class="icon-facebook" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:facebook', linkType:'o' } );"></a></li>
      <li><a href="https://twitter.com/ratemyprofessor" class="icon-twitter" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:twitter', linkType:'o' } );"></a></li>
      <li><a href="http://ratemyprofessors.tumblr.com/" class="icon-tumblr" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:tumblr', linkType:'o' } );"></a></li>
      <li><a href="http://www.pinterest.com/ratemyprofessor/" class="icon-pinterest" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:pinterest', linkType:'o' } );"></a></li>
      <li><a href="http://instagram.com/ratemyprofessors" class="icon-instagram" target="_blank" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'GLOBAL:instagram', linkType:'o' } );"></a></li>
    </ul>
  </div>
  <!-- Ends the Head Social Bar -->
  <div id="desktopLoginSectionContainer" class="processed">
    
	<!-- Need ajax widget -->
	<a href="/member" id="login" class="loggedout">
		<span class="welcome-tablet">Log In</span>
		<span class="welcome"> Log In / Sign Up </span>
	</a>


  </div>
</header>

        <!-- Ends Header -->

        <!-- Starts left Nav -->
        
  <aside id="leftNav" class="height-col">
    <div id="leftOverlay"></div>
    <!-- Starts Left Menus -->
    <div id="menuWrap">


      <!-- Prof Menu -->
      <div id="profMenu" class="menu">
        <div class="header">Edit your professor search</div>
        <div class="prof-block-form">
<div class="center-block-form">
  <div class="h1">Find a Professor</div>
  <div class="search-by" data-search="profMenu">
    <span class="label">SEARCH BY</span>
    <a href="javascript:void(0)" data-type="professor-names" class="active" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Profs_byname', linkType:'o' } );">Name</a>
    <a href="javascript:void(0)" data-type="professor-locations" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Profs_byschool', linkType:'o' } );">School</a>
  </div>
   <form action="/search.jsp?id=prof-name" method="get" name="prof-name" class="professor-names" id="prof-name">
    <input type="hidden" name="queryoption" value="HEADER" id="queryoption">
    <input type="hidden" name="queryBy" value="teacherName" id="queryBy">
    <div class="search-info">
      <div class="optional-flag">
        <span class="line-form-txt">I'm looking for a professor at</span>
        <div class="drop-down-fix">
              <input type="text" id="searchProfessorSchool2" data-type="school" name="schoolName" placeholder="your school" autocorrect="off" autocomplete="off" class="ui-autocomplete-input"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
                <input type="hidden" class="schoolID" name="schoolID" id="nameprofid">
              <div id="profauContainer2" class="autocomplete-container">
               <ul style="display: none;"></ul>
              </div>
                <!-- <span class="optional-content">Optional</span>-->
              </div>

              <span class="line-form-txt">named</span>
        <div class="drop-down-fix">

        <input type="text" name="query" id="searchProfessorName" data-type="name" placeholder="professor's name" autocorrect="off" autocomplete="off" required="" class="ui-autocomplete-input"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
                <div id="profNameAc" class="autocomplete-container">
                  <ul style="display: none;"></ul>
                </div>
                <span class="error-message" id="leftNav_error-message-align">This field is required.</span>
            </div>
        </div>

        <div class="cta">
          <input type="submit" name="_action_search" value="Search" id="prof-name-btn">
          <a class="reset-search-form" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Profs_byname_cancel', linkType:'o' } );">cancel</a>
        </div>
      </div>
   </form>

  <form action="/search.jsp?id=prof-location" method="get" name="prof-location" class="professor-locations" id="prof-location">
    <input type="hidden" name="queryoption" value="TEACHER" id="queryoption">
    <input type="hidden" name="queryBy" value="schoolDetails" id="queryBy">
    <input type="hidden" class="schoolID" name="schoolID">

    <div class="search-info">
      <span class="inline-form-txt">I'm looking for professors at</span>
      <div class="drop-down-fix">
         <input type="text" id="searchProfessorSchool" data-type="school" name="schoolName" placeholder="your school" autocorrect="off" autocomplete="off" required="" onchange="clearDepartmentDropDown();" onkeyup="clearDepartmentDropDown();" class="ui-autocomplete-input"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
         <div id="profauContainer" class="autocomplete-container searchProfessorSchoolAC">
          <ul style="display: none;"></ul>
         </div>
         <span class="error-message" id="leftNav_error-message-align">This field is required.</span>
      </div>
      <div class="h2">in the</div>
      <div class="no-default">
        <span class="sod_select " tabindex="0" data-cycle="false" data-links="false" data-links-external="false" data-placeholder-option="false" data-filter=""><span class="sod_label">select</span><span class="sod_list_wrapper"><span class="sod_list" style="max-height: 36px;"><span class="sod_option  selected active " title="select" data-value="select">select</span></span></span><select name="dept" id="searchProfessorDepartment" data-type="department" data-placeholder-option="false" data-size="10" onchange="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Profs_byschool_deptdropdown', linkType:'o' } );">
          <option>select</option>
        </select></span>
      </div>
      <span class="inline-form-txt"> department.</span>

    <div class="cta">
      <input type="submit" name="_action_search" value="Search" id="prof-location-btn">
      <a class="reset-search-form" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Profs_byschool_cancel', linkType:'o' } );">cancel</a>
    </div>

    </div>
  </form>


   </div>
  </div>
      </div>
      <!-- Ends Prof menu -->

      <!-- School Menu -->
      <div id="schoolMenu" class="menu">
        <div class="header">Find a School</div>
        <div class="school-block-form">
  <div class="center-block-form">
    <div class="h1 mobile-header">Find a School</div>
    <div class="h1 header">Find your school</div>
    <div class="search-by" data-search="schoolMenu">
      <span class="label">SEARCH BY</span>
      <a href="javascript:void(0)" data-type="school-names" class="active" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_byname', linkType:'o' } );">Name</a>
      <a href="javascript:void(0)" data-type="school-locations" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_bylocation', linkType:'o' } );">Location</a>
    </div>
    <form action="/search.jsp?id=schoolNames" method="get" name="schoolNames" class="searchform school-names" id="schoolNames">
      <input type="hidden" name="queryoption" value="HEADER" id="queryoption">
      <input type="hidden" name="queryBy" value="schoolName" id="queryBy">
      <div class="search-info">
        <div class="drop-down-fix">
          <input type="text" onfocus="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_byname_schooltypeahead', linkType:'o' } );" id="schoolName" name="query" placeholder="school's name" autocorrect="off" autocomplete="off" required="" class="ui-autocomplete-input"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
          <div id="schoolauContainer" class="autocomplete-container">
            <ul style="display: none;"></ul>
          </div>
          <span class="error-message" id="leftNav_error-message-align">This field is required.</span>
        </div>
        <div class="info">
          Looking for a professor by school/department?
          <a href="/mobile/professor_search" class="click-here lowercase">Click here.</a>
        </div>
        <div class="cta">
         <input type="submit" value="Search" action="search" id="schoolNames-btn" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_byname_search', linkType:'o' } );">
          <br>
          <a class="reset-search-form">CANCEL</a>
          <div class="left-info">
            Looking for a professor by school/department?
            <a href="/mobile/professor_search" class="click-here lowercase">Click here.</a>
          </div>
        </div>
      </div>
    </form>
    <form action="/search.jsp" method="get" name="schoollocations" class="searchform school-locations" id="schoollocations">
      <input type="hidden" name="queryoption" value="HEADER" id="queryoption">
      <input type="hidden" name="queryBy" value="schoolName" id="queryBy">
      <input type="hidden" name="country" value="united states" id="country">
      <input type="hidden" name="facetSearch" value="true" id="facetSearch">
      <div class="search-info">
        <span class="line-form-txt"><div class="h2">I'm looking for a school in </div></span>
        <div class="select-wraper">
          <span class="sod_select " tabindex="0" data-cycle="false" data-links="false" data-links-external="false" data-placeholder-option="false" data-filter=""><span class="sod_label">select state</span><span class="sod_list_wrapper"><span class="sod_list" style="max-height: 360px;"><span class="sod_option  selected active " title="select state" data-value="">select state</span><span class="sod_option " title="Alaska" data-value="ak">Alaska</span><span class="sod_option " title="Alabama" data-value="al">Alabama</span><span class="sod_option " title="Arkansas" data-value="ar">Arkansas</span><span class="sod_option " title="Arizona" data-value="az">Arizona</span><span class="sod_option " title="California" data-value="ca">California</span><span class="sod_option " title="Colorado" data-value="co">Colorado</span><span class="sod_option " title="Connecticut" data-value="ct">Connecticut</span><span class="sod_option " title="Washington DC" data-value="dc">Washington DC</span><span class="sod_option " title="Delaware" data-value="de">Delaware</span><span class="sod_option " title="Florida" data-value="fl">Florida</span><span class="sod_option " title="Georgia" data-value="ga">Georgia</span><span class="sod_option " title="Hawaii" data-value="hi">Hawaii</span><span class="sod_option " title="Iowa" data-value="ia">Iowa</span><span class="sod_option " title="Idaho" data-value="id">Idaho</span><span class="sod_option " title="Illinois" data-value="il">Illinois</span><span class="sod_option " title="Indiana" data-value="in">Indiana</span><span class="sod_option " title="Kansas" data-value="ks">Kansas</span><span class="sod_option " title="Kentucky" data-value="ky">Kentucky</span><span class="sod_option " title="Louisiana" data-value="la">Louisiana</span><span class="sod_option " title="Massachusetts" data-value="ma">Massachusetts</span><span class="sod_option " title="Maryland" data-value="md">Maryland</span><span class="sod_option " title="Maine" data-value="me">Maine</span><span class="sod_option " title="Michigan" data-value="mi">Michigan</span><span class="sod_option " title="Minnesota" data-value="mn">Minnesota</span><span class="sod_option " title="Missouri" data-value="mo">Missouri</span><span class="sod_option " title="Mississippi" data-value="ms">Mississippi</span><span class="sod_option " title="Montana" data-value="mt">Montana</span><span class="sod_option " title="North Carolina" data-value="nc">North Carolina</span><span class="sod_option " title="North Dakota" data-value="nd">North Dakota</span><span class="sod_option " title="Nebraska" data-value="ne">Nebraska</span><span class="sod_option " title="New Hampshire" data-value="nh">New Hampshire</span><span class="sod_option " title="New Jersey" data-value="nj">New Jersey</span><span class="sod_option " title="New Mexico" data-value="nm">New Mexico</span><span class="sod_option " title="Nevada" data-value="nv">Nevada</span><span class="sod_option " title="New York" data-value="ny">New York</span><span class="sod_option " title="Ohio" data-value="oh">Ohio</span><span class="sod_option " title="Oklahoma" data-value="ok">Oklahoma</span><span class="sod_option " title="Oregon" data-value="or">Oregon</span><span class="sod_option " title="Pennsylvania" data-value="pa">Pennsylvania</span><span class="sod_option " title="Rhode Island" data-value="ri">Rhode Island</span><span class="sod_option " title="South Carolina" data-value="sc">South Carolina</span><span class="sod_option " title="South Dakota" data-value="sd">South Dakota</span><span class="sod_option " title="Tennessee" data-value="tn">Tennessee</span><span class="sod_option " title="Texas" data-value="tx">Texas</span><span class="sod_option " title="Utah" data-value="ut">Utah</span><span class="sod_option " title="Virginia" data-value="va">Virginia</span><span class="sod_option " title="Vermont" data-value="vt">Vermont</span><span class="sod_option " title="Washington" data-value="wa">Washington</span><span class="sod_option " title="Wisconsin" data-value="wi">Wisconsin</span><span class="sod_option " title="West Virginia" data-value="wv">West Virginia</span><span class="sod_option " title="Wyoming" data-value="wy">Wyoming</span></span></span><select onchange="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_bylocation_statedropdown', linkType:'o' } );" id="schoolState" name="stateselect" required="" data-placeholder-option="false" data-size="10">
<option value="">select state</option>
<option value="ak">Alaska</option>
<option value="al">Alabama</option>
<option value="ar">Arkansas</option>
<option value="az">Arizona</option>
<option value="ca">California</option>
<option value="co">Colorado</option>
<option value="ct">Connecticut</option>
<option value="dc">Washington DC</option>
<option value="de">Delaware</option>
<option value="fl">Florida</option>
<option value="ga">Georgia</option>
<option value="hi">Hawaii</option>
<option value="ia">Iowa</option>
<option value="id">Idaho</option>
<option value="il">Illinois</option>
<option value="in">Indiana</option>
<option value="ks">Kansas</option>
<option value="ky">Kentucky</option>
<option value="la">Louisiana</option>
<option value="ma">Massachusetts</option>
<option value="md">Maryland</option>
<option value="me">Maine</option>
<option value="mi">Michigan</option>
<option value="mn">Minnesota</option>
<option value="mo">Missouri</option>
<option value="ms">Mississippi</option>
<option value="mt">Montana</option>
<option value="nc">North Carolina</option>
<option value="nd">North Dakota</option>
<option value="ne">Nebraska</option>
<option value="nh">New Hampshire</option>
<option value="nj">New Jersey</option>
<option value="nm">New Mexico</option>
<option value="nv">Nevada</option>
<option value="ny">New York</option>
<option value="oh">Ohio</option>
<option value="ok">Oklahoma</option>
<option value="or">Oregon</option>
<option value="pa">Pennsylvania</option>
<option value="ri">Rhode Island</option>
<option value="sc">South Carolina</option>
<option value="sd">South Dakota</option>
<option value="tn">Tennessee</option>
<option value="tx">Texas</option>
<option value="ut">Utah</option>
<option value="va">Virginia</option>
<option value="vt">Vermont</option>
<option value="wa">Washington</option>
<option value="wi">Wisconsin</option>
<option value="wv">West Virginia</option>
<option value="wy">Wyoming</option>
</select></span>
        </div>
        <span class="error-message" id="leftNav_error-message-align">This field is required.</span>
      </div>
      <div class="info">
        Looking for a professor by school/department?
        <a href="/mobile/professor_search" class="click-here lowercase">Click here.</a>
      </div>
      <div class="cta">
        <input type="submit" id="schoolLocationz" name="schoolLocationz" value="Search" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:School_bylocation_search', linkType:'o' } );">
        <a class="reset-search-form">CANCEL</a>
      </div>
    </form>
  </div>
</div>


      </div>
      <!-- Ends school menu -->

      <!-- Rate Menu -->
      <div id="rateMenu" class="menu">

        <div class="header">Rate a</div>
        <div class="school-block-form">
  <div class="h1">Rate a</div>
  <div class="search-by" data-search="rateMenu">
    <a href="javascript:void(0)" data-type="rate-professor" class="active" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Rate_Prof', linkType:'o' } );">Professor</a>
    <a href="javascript:void(0)" data-type="rate-schools" class="" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'LEFTNAV:Rate_School', linkType:'o' } );">School</a>
  </div>
  <form action="/search.jsp?id=rateProfessor" method="get" name="rateProfessor" class="searchform rate-professor" style="" id="rateProfessor">
    <input type="hidden" name="queryoption" value="HEADER" id="queryoption">
    <input type="hidden" name="queryBy" value="teacherName" id="queryBy">
    <div class="search-info">
      <span class="wrap">
        I want to rate <br>
        <input type="text" id="rateProfessorAC" name="query" placeholder="Professor's Name" required="" class="ui-autocomplete-input" autocomplete="off"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
        <span class="error-message">This field is required.</span>
        <div id="rateProfAC" class="autocomplete-container">
          <ul style="display: none;"></ul>
        </div>
      </span>
    </div>
    <div class="cta">
      <input type="submit" value="Search" id="rateProfessor-btn"> <br>
      <a class="reset-search-form">cancel</a>
    </div>
  </form>
  <form action="/search.jsp?id=rateSchool" method="get" name="rateSchool" class="searchform rate-schools" style="" id="rateSchool">
    <input type="hidden" name="queryoption" value="HEADER" id="queryoption">
    <input type="hidden" name="queryBy" value="schoolName" id="queryBy">
    <div class="search-info">
      <span class="wrap">
        I want to rate <br>
        <input type="text" id="schoolName" name="query" placeholder="School's Name" required="" class="ui-autocomplete-input" autocomplete="off"><span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span>
        <span class="error-message">This field is required.</span>
        <div id="rateSchoolAC" class="autocomplete-container">
          <ul style="display: none;"></ul>
        </div>
      </span>
    </div>
    <div class="cta">
      <input type="submit" value="Search" id="rateSchool-btn"> <br>
      <a class="reset-search-form">cancel</a>
    </div>
  </form>
</div>
      </div>
      <!-- Ends Rate Menu -->

      <!-- Blog Menu -->
      
  	    <div id="blogMenu" class="menu js-blog-menu-global">
  	      <div class="blogMenu-inner">
  		      <div class="header">Rate My Professors Blog</div>
  		      <a class="close-left-nav close-this">×</a>
<div class="clearfix"></div>
<div class="panel-filter">
  <div class="result-count">
    <div class="sort-option">
      
        <span class="sod_select " tabindex="0" data-cycle="false" data-links="false" data-links-external="false" data-placeholder-option="false" data-filter=""><span class="sod_label">All Categories</span><span class="sod_list_wrapper"><span class="sod_list" style="max-height: 170px;"><span class="sod_option  selected active " title="All Categories" data-value="All">All Categories</span><span class="sod_option " title="RMP Buzz" data-value="RMP Buzz">RMP Buzz</span><span class="sod_option " title="Video" data-value="Professors Strike Back">Video</span><span class="sod_option " title="Top Lists" data-value="Lists">Top Lists</span><span class="sod_option " title="Miscellaneous" data-value="Misc.">Miscellaneous</span></span></span><select id="blog-filter" name="blogfilter" class="blog-filters">
<option value="All">All Categories</option>
<option value="RMP Buzz">RMP Buzz</option>
<option value="Professors Strike Back">Video</option>
<option value="Lists">Top Lists</option>
<option value="Misc.">Miscellaneous</option>
</select></span>
      
		</div>
  </div>
</div>
<div class="result-list">
  <ul id="blog-item-list">
    <li>
      <a href="/blog/buzzpost/yoda-legendary-jedi-warrior/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/12/yoda-thumbnail.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>Yoda may be a legendary Jedi warrior, but is he a solid professor?</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/misc/new-episodes-of-wild-n-out-starting-wednesday-december-16th/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/12/WNOs7_RMPHomepageBlock_72x72.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Miscellaneous</span>
          </div>
          <p>New episodes of ‘Wild ‘N Out’ starting Wednesday, Dec. 16th!</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/buzzpost/dont-revenge-rate-pro-tips/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/12/dosdontsthumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>Don’t “revenge rate” and other pro tips for rating your professors this semester.</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/buzzpost/bond-professor-bond/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/11/jb-thumb.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>Are these “Professor Bonds” highly trained MI6 agents…or just professors?</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/buzzpost/what-happens-when-you-dont-rate/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/10/omg-catthumb-e1446056586908.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>What happens to Rate My Professors when you don’t rate? (Hint: it’s not pretty)</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/buzzpost/get-excited-its-back-to-the-future-day/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/10/Emmett_Brown_2-e1445448472158.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>Get excited: it’s “Back to the Future day!”</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/video/albion-college-professors-read-their-ratings-part-2/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Albionpt2thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Video</span>
          </div>
          <p>Albion College Professors Read Their Ratings – Part 2</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/2014-2015-top-lists/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>The 2014-2015 Annual Top Lists Are Here!</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/top-universities-of-2014-2015/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>Highest Rated Universities of 2014-2015</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/top-jr-colleges-2014-2015/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>Highest Rated Junior and Community Colleges of 2014-2015</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/top-professors-of-2014-2015/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>Highest Rated University Professors of 2014-2015</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/top-jr-college-professors-of-2014-2015/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>Highest Rated Junior and Community College Professors of 2014-2015</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/hottest-professors-of-2014-2015/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>Hottest Professors of 2014-2015</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/toplist/the-most-fun-lists/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/Top-List-Thumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Lists</span>
          </div>
          <p>The Most Fun Lists</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/video/university-of-ottawa-professors-read-their-ratings/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/ottawathumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Video</span>
          </div>
          <p>University of Ottawa Professors Read Their Ratings</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/video/marywood-university-professors-read-their-ratings/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/09/marywoodthumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Video</span>
          </div>
          <p>Marywood University Professors Read Their Ratings</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/video/st-johns-university-professors-read-their-ratings-2/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/08/FeinsteinStjohns-e1440708795181.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Video</span>
          </div>
          <p>St. John’s University Professors Read Their Ratings</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/buzzpost/when-back-to-school-season-punches-you-in-the-face-2/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/08/Helga-Punchthumb.png" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>RMP Buzz</span>
          </div>
          <p>When Back to School Season Punches You in the Face</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/misc/amazon-student-awarding-250000-in-scholarships/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/06/ratemyprofessor-72x72_color-optimized.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Miscellaneous</span>
          </div>
          <p>Amazon Student Awarding $250,000 in Scholarships</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  
    <li>
      <a href="/blog/misc/food-to-get-you-laid-premieres-friday-august-14-at-930p/">
        <figure><img src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/08/logo_ftgyl_72x72-rmp.jpg" width="73" height="73"></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>Miscellaneous</span>
          </div>
          <p>Food To Get You Laid Premieres Friday August 14 at 9:30p</p>
        </div>
      </a>
      <div class="clearfix"></div>
    </li>
  </ul>
  <input type="submit" value="LOAD MORE" id="loadmoreBlog" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'BLOG:LoadMore', linkType:'o' } );">

  <!-- Blog item templates -->
  <script type="text/template" id="blogitems">
    <li>
      <a href="/{{actionUrl}}{{blogurl}}">
        <figure><img src="{{imageurl}}" width="73" height="73" /></figure>
        <div class="text-wrap">
          <div class="tag">
            <span>{{category}}</span>
          </div>
          <p>{{title}}</p>
        </div>
      </a>
      <div class = "clearfix"></div>
    </li>
  </script>
</div>

  	   	  </div>
  	    </div>
       
      <!-- Ends Blog Menu -->

	 
      <!-- My Profs Menu -->
	      <div id="myProfsMenu" class="menu">
	        <a class="close-left-nav close-this">×</a>
<div class="header">My Professors</div>
<hr>
<div class="my-professors-result-list">
  <ul>
  </ul>
  <p class="no-professors"></p>
</div>

<div class="myProfprogressbtnwrap" data-search-type="search">
  <a href="#" class="content" id="myProfloadMore" data-teach-id="1981141" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:LoadMore', linkType:'o' } );">Load More</a>
  <div class="progress-bar"></div>
</div>

<script type="text/template" id="my-professor-result-template">
  <li id = "my-professor-{{id}}">
    <a href="/ShowRatings.jsp?tid={{id}}&showMyProfs=true">
      <span class="{{ratingclass}}-icon"></span>
      <span class="remove-this-button" data-id="{{id}}">&#215;</span>
      <span class="rating">{{overall_rating}}</span>
      <span class="name">{{plname}}, {{{pfname}}}
        <span class="info">{{rating_count}} RATINGS</span>
      </span>
    </a>
  </li>
</script>
	      </div>
      <!-- Ends My Profs Menu -->

    </div>
    <!-- Ends Left Menu -->

    <!-- Starts Left Nav -->
    <nav id="navToggle">
      <ul>

        <li>
          <a href="#" class="menu-item highlighted blocked" id="profNav" data-menu="profMenu">
            <span class="icon icon-professor"></span>
            <span class="label">Profs</span>
          </a>
        </li>
        <li>
          <a href="#" class="menu-item" id="schoolNav" data-menu="schoolMenu">
            <span class="icon icon-school"></span>
            <span class="label">School</span>
          </a>
        </li>
        <li>
          <a href="#" class="menu-item" data-menu="rateMenu">
            <span class="icon icon-rate"></span>
            <span class="label">Rate</span>
          </a>
        </li>
        <li>
          <a href="#" class="menu-item" id="blogNav" data-menu="blogMenu">
            <span class="icon icon-blog"></span>
            <span class="label">Blog</span>
          </a>
        </li>
        
        <li id="desktopmyProfContainer" class="hide">
            <a href="#" class="menu-item" data-menu="myProfsMenu">
                <div class="my-prof-notice">Click here to see all your saved professors.</div>
                <span class="icon icon-my-profs"></span>
                <span class="label">My Profs</span>
            </a>
         </li>
        
      </ul>

    </nav>
    <!-- Ends left Nav -->

  </aside>

        <!-- Ends Left Nav -->
      

      <!-- Starts Body Content -->

      <div id="body" class="slide" style="margin-top: 72px;">
        <div id="mainContent" class="height-col">
          
    <div class="right-panel">
      <div class="top-info-block">
        <div class="result-image">
          
        </div>
        <div class="result-info">
          <div class="result-name">
          <h1 class="profname">
            <span class="pfname"> Alex</span> <span class="pfname"> </span> <span class="plname">
              Smith
            </span>
          </h1>
            
          </div>
          <div class="result-title">
            Professor in the Biology department
            <br>
            <h2 class="schoolname">at <a href="/campusRatings.jsp?sid=1426" class="school">University of Guelph</a>, Guelph, ON</h2>
          </div>
          

          
            
              <a href="/joinprof.jsp" id="areyouquestion" style="display: inline;">are you Alex Smith?</a>
            
          
        </div>
        
        
        <div class="actions">
          
            <a href="/AddRating.jsp?tid=1981141" class="rate" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Rate_top', linkType:'o' } )">Rate this professor</a>
            <div class="share">
              Share
              <div class="share-intent">
                <a class="desktop intent-facebook icon-facebook" target="_blank" href="http://www.facebook.com/sharer.php?s=100&amp;p[url]=www.ratemyprofessors.com/ShowRatings.jsp?tid=1981141" onclick="window.open(this.href,'targetWindow','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600px,height=300px');  javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Facebook', linkType:'o' } ); return false;"></a>
                <a class="mobile-block intent-facebook icon-facebook" target="_blank" href="http://m.facebook.com/sharer.php?s=100&amp;u=www.ratemyprofessors.com/ShowRatings.jsp?tid=1981141" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Facebook, linkType:'o' } ); return false;"></a>
                <a href="https://twitter.com/intent/tweet?text=You%27ve gotta check out Alex Smith on %40RateMyProfessor - www.ratemyprofessors.com%2FShowRatings.jsp%3Ftid%3D1981141" target="_blank" class="intent-twitter icon-twitter" onclick="window.open(this.href,'targetWindow','toolbar=no,location=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=600px,height=300px'); javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Twitter', linkType:'o' } ); return false;"></a>
              </div>
            </div>
          
          <div class="links">
            <a href="/submitCorrection.jsp?tid=1981141" class="correction">Submit a Correction</a>
            <a href="/help.jsp#tally" class="correction">| Learn how ratings work</a>
          </div>
        </div>
        <div id="ad-container" class="right-panel-mtvnad"><div id="coda_ad_300x250_6" data-ad-sizes="300x250" data-ad-keyvalues="gridAd=grid"></div></div>
      </div>
      <div class="rating-breakdown">
        <div class="left-breakdown">
          <div class="breakdown-wrapper">
            <div class="breakdown-header">
              Overall Quality
              <div class="grade">4.5</div>
            </div>
            <div class="breakdown-header" title="Refers to the average grade raters received">
              Raters' Avg. Grade
              <div class="grade">N/A</div>
            </div>
            <div class="breakdown-header">
              Hotness
              <div class="grade">
                <figure>
                  <img src="/assets/chilis/cold-chili.png" width="70">
                </figure>
              </div>
            </div>
          </div>
          
            <div class="faux-slides">
          
            <div class="rating-slider">
              <div class="label">Helpfulness</div>
              <div class="rating">4.5</div>
              <div class="slider">
                <div class="rate-slider" data-rating="good">
                  <div class="ui-slider-range" style="width:90.0%"></div>
                  <a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 90.0%;"></a>
                </div>
              </div>
            </div>
            <div class="rating-slider">
              <div class="label">Clarity</div>
              <div class="rating">4.5</div>
              <div class="slider">
                <div class="rate-slider" data-rating="good">
                  <div class="ui-slider-range" style="width:90.0%"></div>
                  <a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 90.0%;"></a>
                </div>
              </div>
            </div>
            <div class="rating-slider">
              <div class="label">Easiness</div>
              <div class="rating">3.5</div>
              <div class="slider">
                <div class="rate-slider" data-rating="average">
                  <div class="ui-slider-range" style="width:70.0%"></div>
                  <a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 70.0%;"></a>
                </div>
              </div>
            </div>
          </div>
          <div class="edit-slides">
            <form action="/AddRating.jsp?tid=1981141" method="post" name="rateProfessorForm" class="rate" id="rateProfessorForm">
              <div class="rating-slider-wrapper">
                <div class="rating-slider">
                  <div class="label">Helpfulness</div>
                  <div class="rating">0</div>
                  <div class="slider">
                    <div id="helpfulnessSlider" data-value="0" class="rate-slider ui-slider ui-slider-horizontal ui-widget ui-widget-content ui-corner-all" data-rating="start"><div class="ui-slider-range ui-widget-header ui-slider-range-min" style="width: 0%;"></div><a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 0%;"><div class="bubble" style="background-position: 63px 20px;width:120px;"><span class="text">Drag Here</span></div></a></div>
                    <input type="hidden" name="helpfulnessrating" id="helpfulnessrating" value="0">
                    <div class="bubble-text" data-bub1="No help here" data-bub2="You have to beg for help" data-bub3="If you ask for help, it’s there" data-bub4="Most likely to help" data-bub5="Saved my semester">
                    </div>
                  </div>
                </div>
                <div class="rating-slider">
                  <div class="label">Clarity</div>
                  <div class="rating">0</div>
                  <div class="slider">
                    <div id="claritySlider" data-value="0" class="rate-slider ui-slider ui-slider-horizontal ui-widget ui-widget-content ui-corner-all" data-rating="start"><div class="ui-slider-range ui-widget-header ui-slider-range-min" style="width: 0%;"></div><a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 0%;"><div class="bubble" style="background-position: 63px 20px;width:120px;"><span class="text">Drag Here</span></div></a></div>
                    <input type="hidden" name="clarityrating" id="clarityrating" value="0">
                    <div class="bubble-text" data-bub1="Say what??" data-bub2="Confusing" data-bub3="Pretty clear" data-bub4="Clear-cut" data-bub5="Crystal-clear">
                    </div>
                  </div>
                </div>
                <div class="rating-slider">
                  <div class="label">Easiness</div>
                  <div class="rating">0</div>
                  <div class="slider">
                    <div id="easinessSlider" data-value="0" class="rate-slider ui-slider ui-slider-horizontal ui-widget ui-widget-content ui-corner-all" data-rating="start"><div class="ui-slider-range ui-widget-header ui-slider-range-min" style="width: 0%;"></div><a class="ui-slider-handle ui-state-default ui-corner-all" href="#" style="left: 0%;"><div class="bubble" style="background-position: 63px 20px;width:120px;"><span class="text">Drag Here</span></div></a></div>
                    <input type="hidden" name="easinessrating" id="easinessrating" value="0">
                    <div class="bubble-text" data-bub1="Hardest thing I've ever done" data-bub2="Makes you work for it" data-bub3="The usual" data-bub4="Easy A" data-bub5="Show up &amp; pass">
                    </div>
                  </div>
                </div>
              </div>
              <div class="slider-action-wrapper">
                <input type="submit" value="Continue" name="sliderValues" id="sliderValues" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Sliders_Continue', linkType:'o' } );" disabled="">
                <a href="#" class="cancel" id="cancel-rating" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Sliders_Cancel', linkType:'o' } );">cancel</a>
              </div>
            </form>
          </div>
        </div>
        <div class="right-breakdown">
          <div class="tag-box-header">Top 20 Tags for this Professor</div>
          <p>See how other students describe this professor.</p>
          <div class="tag-box">
            
              <span class="tag-box-choosetags"> Would take again <b>(1)</b></span>
            
              <span class="tag-box-choosetags"> Hilarious <b>(1)</b></span>
            
              <span class="tag-box-choosetags"> Inspirational <b>(1)</b></span>
            
          </div>
          
            <a href="#" data-animation="none" data-reveal-id="chooseTagModal" class="choosetags" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Tags', linkType:'o' } );">Choose your tags</a>
          
        </div>
      </div>
      <div id="mobile-ad-container" class="phone--add first--one" style="text-align:center;"></div>
      <div class="table-toggle rating-count active" data-table="rating-filter">
        2 Student Ratings
      </div>
      <div class="table-toggle professor-note" data-table="professor-notes" style="display:none" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Notes', linkType:'o' } );">
        
          0 Professor's Notes
        
      </div>
      <form action="/AddRating.jsp?tid=1981141" method="post" name="sratingCommentForm" id="sratingCommentForm">
      <div class="srating-Comments-text">
        <div class="input">
          <div class="input">
            <textarea name="sratingComments" id="sratingComments" class="field autoExpand" rows="1" maxlength="350" placeholder="Start typing your comment..."></textarea>
            <div id="noteCount" class="character-count"><span>350</span> characters left</div>
          </div>
          <input type="hidden" name="fromContinueRating" id="fromContinueRating" class="field" value="1">
        </div>
        <div class="submit-form">
          <input type="submit" value="Continue Your Rating" name="sratingSubmit" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:CommentContinue', linkType:'o' } );" id="sratingSubmit">
        </div>
      </div>

    </form>
      <!-- If there is a note Show it -->
      <!-- Ends the note -->
      <div class="rating-filter togglable">
        <table class="tftable" border="0">
          <tbody><tr>
            <th class="head-label rating-level rating">
              <span class="sort-type" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:SortRatings', linkType:'o' } );">Rating: <span class="class-code">All</span></span>
              <span class="selected-type"></span>
              <div class="drop-down" id="ratingDrop" data-sort-type="rating">
                <div class="drop-wrap">
                  <div class="option rating-all" data-sortby="rating-all">
                    <span class="icon-title">All Ratings</span>
                  </div>
                  <div class="option " data-sortby="rating-good">
                    <span class="icon good-icon"></span>
                    <span class="icon-title">Good</span>
                  </div>
                  <div class="option" data-sortby="rating-average">
                    <span class="icon average-icon"></span>
                    <span class="icon-title">Average</span>
                  </div>
                  <div class="option" data-sortby="rating-poor">
                    <span class="icon poor-icon"></span>
                    <span class="icon-title">Poor</span>
                  </div>
                </div>
              </div>
            </th>
            <th class="head-label class">
              <span class="sort-type">Class</span>
              <span class="selected-type"></span>
              
            </th>
            <th class="comment-nodropdown">
              <span class="sort-type">Comment</span>
            </th>
          </tr>
          <!-- Iterate Through professor Ratings -->
          
          
            
            <tr id="24465925" class="">
              <td class="rating">
                <div class="date"> 03/16/2015</div>
                <div class="rating-block good">
                  <div class="rating-wrapper">
                    <div class="icon good-icon"></div>
                    <span class="rating-type">good</span>
                  </div>
                  <div class="breakdown">
                    <div class="break">
                      <span class="score good">4</span>
                      <span class="descriptor">Helpfulness</span>
                    </div>
                    <div class="break">
                      <span class="score good">5</span>
                      <span class="descriptor">Clarity</span>
                    </div>
                    <div class="break">
                      <span class="score good">5</span>
                      <span class="descriptor">Easiness</span>
                    </div>
                  </div>
                </div>
              </td>
              <td class="class">
                <span class="name "> <span class="response">ZOO2700</span></span>
                <span class="credit">For Credit: <span class="response">Yes</span></span>
                <span class="attendance">Attendance: <span class="response">Mandatory</span></span>
                <span class="textbook-use">Textbook Use: <span class="response">Essential to passing</span></span>
                <span class="rater-interest">Rater Interest: <span class="response">Really into it</span></span>
                <span class="grade">Grade Received: <span class="response">Not sure yet</span></span>
              </td>
              
               <td class="comments">
               <div class="tagbox">
                  
                     <span>HILARIOUS</span>
                  
                     <span>INSPIRATIONAL</span>
                  
                     <span>WOULD TAKE AGAIN</span>
                  
               </div>

                <p class="commentsParagraph">
                   He's absolutely hilarious, and engaging. The course content is not always interesting but he is always enthusiastic and exciting.  Not just my favorite prof but one of my favorite teachers I've ever had.
                </p>

                
                  <div class="helpful-links thumbs">
                    <a href="#" data-id="24465925" data-url="/teacherRating/updateTeacherRatingHelp/24465925" data-tid="1981141" class="helpful" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Useful', linkType:'o' } );"><span class="count">
                        0
                    </span> <span class="grouping">people</span>
                      found this useful </a>
                    <a href="#" data-id="24465925" data-url="/teacherRating/updateTeacherRatingHelp/24465925" data-tid="1981141" class="nothelpful" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:NotUseful', linkType:'o' } );"><span class="count">
                        0
                    </span> <span class="grouping">people</span>
                      did not find this useful</a>
                  </div>
                
                <div class="helpful-links">
                  
                    <a href="/flagTeacherRating.jsp?rid=24465925" class="report" data-report-text="He's absolutely hilarious, and engaging. The course content is not always interesting but he is always enthusiastic and exciting.  Not just my favorite prof but one of my favorite teachers I've ever had. ">report this rating</a>
                  
                </div>
              </td>
            

            </tr>
            
          
            
            <tr id="24347978" class="even">
              <td class="rating">
                <div class="date"> 01/30/2015</div>
                <div class="rating-block good">
                  <div class="rating-wrapper">
                    <div class="icon good-icon"></div>
                    <span class="rating-type">good</span>
                  </div>
                  <div class="breakdown">
                    <div class="break">
                      <span class="score good">5</span>
                      <span class="descriptor">Helpfulness</span>
                    </div>
                    <div class="break">
                      <span class="score good">4</span>
                      <span class="descriptor">Clarity</span>
                    </div>
                    <div class="break">
                      <span class="score average">2</span>
                      <span class="descriptor">Easiness</span>
                    </div>
                  </div>
                </div>
              </td>
              <td class="class">
                <span class="name "> <span class="response">ZOO2700</span></span>
                <span class="credit">For Credit: <span class="response">Yes</span></span>
                <span class="attendance">Attendance: <span class="response">N/A</span></span>
                <span class="textbook-use">Textbook Use: <span class="response">It's a must have</span></span>
                <span class="rater-interest">Rater Interest: <span class="response">It's my life</span></span>
                <span class="grade">Grade Received: <span class="response">N/A</span></span>
              </td>
              
               <td class="comments">
               <div class="tagbox">
                  
               </div>

                <p class="commentsParagraph">
                   Super awesome prof, he's really enthusiastic even when the students aren't. He plays a lot of interesting videos to get people engaged with boring invertebrate stuff. He's hilarious but a really good teacher, I would hate the class if he wasn't teaching it
                </p>

                
                  <div class="helpful-links thumbs">
                    <a href="#" data-id="24347978" data-url="/teacherRating/updateTeacherRatingHelp/24347978" data-tid="1981141" class="helpful" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Useful', linkType:'o' } );"><span class="count">
                        0
                    </span> <span class="grouping">people</span>
                      found this useful </a>
                    <a href="#" data-id="24347978" data-url="/teacherRating/updateTeacherRatingHelp/24347978" data-tid="1981141" class="nothelpful" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:NotUseful', linkType:'o' } );"><span class="count">
                        0
                    </span> <span class="grouping">people</span>
                      did not find this useful</a>
                  </div>
                
                <div class="helpful-links">
                  
                    <a href="/flagTeacherRating.jsp?rid=24347978" class="report" data-report-text="Super awesome prof, he's really enthusiastic even when the students aren't. He plays a lot of interesting videos to get people engaged with boring invertebrate stuff. He's hilarious but a really good teacher, I would hate the class if he wasn't teaching it">report this rating</a>
                  
                </div>
              </td>
            

            </tr>
            
          
        </tbody></table>
        
        <div class="filter-no-ratings">
          <p>No ratings found – <a href="#" class="filter-reset">view all ratings</a> for this professor.</p>
        </div>
        <div class="helpfulReviewBanner">
          
            <div class="text">Were these reviews helpful? Help out your fellow students.</div>
            <a href="/AddRating.jsp?tid=1981141" class="rate" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Rate_bottom', linkType:'o' } )">Rate this professor</a>
          
        </div>
        <div class="more-from-prof-container">
          <a href="/search.jsp?queryoption=TEACHER&amp;schoolName=University of Guelph&amp;schoolID=1426&amp;dept=&amp;queryBy=schoolDetails&amp;query=*&amp;stateselect=&amp;country=&amp;max=20">
            <span class="more-from-prof"><i class="icon--arow-sm"></i>More Professors from this school</span>
          </a>
        </div>
      </div>
      <!-- Starts The Note Table -->
      <div class="professor-notes togglable">
        <!-- This should only be added to the view if the current user matches the profile id -->

          <!-- need to add if condition here such that below should disaply only when prof logged in and tid = tpid -->
          <div class="addNote" style="display:none">
            <div class="header">Add your notes</div>
            <div class="form-wrap">
              <form action="save/1981141" id="noteForm" method="post" data-id="1981141">
                <input type="hidden" name="tid" value="1981141" id="tid">
                <input type="hidden" name="mode" value="insert" id="mode">
                <input type="hidden" name="rebuttalTotal" value="0" id="rebuttalTotal">
                <div class="form-element">
                  <label>Class</label>
                  <div class="error"></div>
                  <div class="input">
                    <input type="text" name="course" placeholder="Course number" value="">
                  </div>
                </div>
                <div class="form-element">
                  <label>Comment</label>
                  <div class="error"></div>
                  <div class="input">
                    <div id="noteCount" class="character-count"><span>350</span> characters left</div>
                    <textarea id="professorNote" name="comments" maxlength="350"></textarea>
                  </div>
                </div>
                <div class="legal">
                  By clicking the 'Submit' button, I acknowledge that I have read and agreed to the Rate My Professors
                  <a href="/TermsOfUse_us.jsp#guidelines" target="_blank">Site Guidelines</a>,
                  <a href="/TermsOfUse_us.jsp#use" target="_blank">Terms of Use</a> and
                  <a href="/TermsOfUse_us.jsp#privacy" target="_blank">Privacy Policy</a>.
                  Submitted data becomes the property of RateMyProfessors.com. IP addresses are logged.
                </div>
                <div class="clearfix"></div>
                <input type="submit" id="noteAdd" name="noteAdd" value="submit" data-reveal-id="saveNoteModal">
              </form>
            </div>
          </div>
        <!-- This should only be added to the view if the current user matches the profile id -->
        <table class="tftable" border="0">
          <tbody><tr>
            <th class="head-label" width="220px">date</th>
            <th class="head-label" width="255px">Class</th>
            <th class="head-label">Note</th>
          </tr>
          
        </tbody></table>
        
      </div>
      <!-- Ends: Note Table -->
    </div>
    <div class="left-panel" data-teach-id="1981141" data-param-schoolid="1426" data-schoolid="1426" data-param-department="Biology" data-rebuttaltotal="0" data-userid="" data-proftpid="" data-tpid=""><a class="toggle-left-panel close-this">×</a>
      <div class="side-panel">
        <div>
          Showing professors at
        </div>
        <div>
          <span class="school-name">University of Guelph</span> <a id="edit" href="javascript:void(0)" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:Edit', linkType:'o' } );">Edit</a>
        </div>
        <div class="department-combobox">
          in
          <div class="combobox-container combobox-selected"> <input type="hidden" value="Biology" name=""> <div class="input-group"> <input type="text" autocomplete="off" autocorrect="off" spellcheck="false" placeholder="Enter Your Department" class="combobox"> <span class="input-group-addon dropdown-toggle" data-dropdown="dropdown"> <span class="caret"></span> <span class="glyphicon glyphicon-remove"></span> </span> </div> </div><select class="combobox" id="department-dropdown" onchange="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:ComboBox', linkType:'o' } );" style="display: none;">
            <option value="">Enter Your Department</option>
            
              
                <option value="Accounting">Accounting</option>
              
            
              
                <option value="Agribusiness">Agribusiness</option>
              
            
              
                <option value="Agricultural Sciences">Agricultural Sciences</option>
              
            
              
                <option value="Agriculture">Agriculture</option>
              
            
              
                <option value="Animal Science">Animal Science</option>
              
            
              
                <option value="Anthropology">Anthropology</option>
              
            
              
                <option value="Architecture">Architecture</option>
              
            
              
                <option value="Art">Art</option>
              
            
              
                <option value="Behavioral &amp; Social Sciences">Behavioral &amp; Social Sciences</option>
              
            
              
                <option value="Biology" selected="selected">Biology</option>
              
            
              
                <option value="Biomedical">Biomedical</option>
              
            
              
                <option value="Business">Business</option>
              
            
              
                <option value="Chemistry">Chemistry</option>
              
            
              
                <option value="Classics">Classics</option>
              
            
              
                <option value="Communication">Communication</option>
              
            
              
                <option value="Computer Science">Computer Science</option>
              
            
              
                <option value="Criminal Justice">Criminal Justice</option>
              
            
              
                <option value="Culinary Arts">Culinary Arts</option>
              
            
              
                <option value="Design">Design</option>
              
            
              
                <option value="Ecology">Ecology</option>
              
            
              
                <option value="Economics">Economics</option>
              
            
              
                <option value="Education">Education</option>
              
            
              
                <option value="Engineering">Engineering</option>
              
            
              
                <option value="English">English</option>
              
            
              
                <option value="Environmental Engineering">Environmental Engineering</option>
              
            
              
                <option value="Environmental Science">Environmental Science</option>
              
            
              
                <option value="Environmental Studies">Environmental Studies</option>
              
            
              
                <option value="Ethnic Studies">Ethnic Studies</option>
              
            
              
                <option value="Family &amp; Human Studies">Family &amp; Human Studies</option>
              
            
              
                <option value="Film">Film</option>
              
            
              
                <option value="Finance">Finance</option>
              
            
              
                <option value="Food Science">Food Science</option>
              
            
              
                <option value="Food Science &amp; Nutrition">Food Science &amp; Nutrition</option>
              
            
              
                <option value="Geography">Geography</option>
              
            
              
                <option value="Geology">Geology</option>
              
            
              
                <option value="Gerontology">Gerontology</option>
              
            
              
                <option value="Graphic Arts">Graphic Arts</option>
              
            
              
                <option value="Health Science">Health Science</option>
              
            
              
                <option value="History">History</option>
              
            
              
                <option value="Hospitality">Hospitality</option>
              
            
              
                <option value="Human Development">Human Development</option>
              
            
              
                <option value="Human Kinetics">Human Kinetics</option>
              
            
              
                <option value="Human Resources">Human Resources</option>
              
            
              
                <option value="Humanities">Humanities</option>
              
            
              
                <option value="Information Science">Information Science</option>
              
            
              
                <option value="International Studies">International Studies</option>
              
            
              
                <option value="Journalism">Journalism</option>
              
            
              
                <option value="Kinesiology">Kinesiology</option>
              
            
              
                <option value="Landscape Architecture &amp; Regional Planning">Landscape Architecture &amp; Regional Planning</option>
              
            
              
                <option value="Languages">Languages</option>
              
            
              
                <option value="Law">Law</option>
              
            
              
                <option value="Literature">Literature</option>
              
            
              
                <option value="Management">Management</option>
              
            
              
                <option value="Marketing">Marketing</option>
              
            
              
                <option value="Mathematics">Mathematics</option>
              
            
              
                <option value="Medicine">Medicine</option>
              
            
              
                <option value="Molecular/Cellular Biology">Molecular/Cellular Biology</option>
              
            
              
                <option value="Music">Music</option>
              
            
              
                <option value="Nursing">Nursing</option>
              
            
              
                <option value="Philosophy">Philosophy</option>
              
            
              
                <option value="Physical Education">Physical Education</option>
              
            
              
                <option value="Physics">Physics</option>
              
            
              
                <option value="Political Science">Political Science</option>
              
            
              
                <option value="Psychology">Psychology</option>
              
            
              
                <option value="Science">Science</option>
              
            
              
                <option value="Social Science">Social Science</option>
              
            
              
                <option value="Social Work">Social Work</option>
              
            
              
                <option value="Sociology">Sociology</option>
              
            
              
                <option value="Sociology &amp; Anthropology">Sociology &amp; Anthropology</option>
              
            
              
                <option value="Statistics">Statistics</option>
              
            
              
                <option value="Studio Art">Studio Art</option>
              
            
              
                <option value="Theater">Theater</option>
              
            
              
                <option value="Tourism Management">Tourism Management</option>
              
            
              
                <option value="Tourism Studies">Tourism Studies</option>
              
            
              
                <option value="Women's Studies">Women's Studies</option>
              
            
              
                <option value="Writing">Writing</option>
              
            
          </select>
        </div>
        <!--googleoff: index-->
<div class="panel-filter">
  <div class="sort-options">
    <span class="professor-count">71</span> professors found
    <span class="sod_select " tabindex="0" data-cycle="false" data-links="false" data-links-external="false" data-placeholder-option="false" data-filter=""><span class="sod_label">Please select</span><span class="sod_list_wrapper"><span class="sod_list" style="max-height: 231px;"><span class="sod_option  selected active " title="Please select" data-value="">Please select</span><span class="sod_option " title="Most Rated" data-value="total_number_of_ratings_i desc">Most Rated</span><span class="sod_option " title="Highest Rated" data-value="averageratingscore_rf desc,total_number_of_ratings_i desc">Highest Rated</span><span class="sod_option " title="Most Helpful" data-value="averagehelpfulscore_rf desc">Most Helpful</span><span class="sod_option " title="Clearest" data-value="averageclarityscore_rf desc">Clearest</span><span class="sod_option " title="Easiest" data-value="averageeasyscore_rf desc">Easiest</span><span class="sod_option " title="Alphabetical" data-value="teacherlastname_sort_s asc">Alphabetical</span></span></span><select id="sort-results" onchange="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:Sort', linkType:'o' } );">
      <!--
        use cookies to determine which sort is selected
        we also unfortunately have to replace html encoded spaces
        since cookies are url encoded
      -->
      <option value="">Please select</option>
      <option value="total_number_of_ratings_i desc">Most Rated</option>
      <option value="averageratingscore_rf desc,total_number_of_ratings_i desc">Highest Rated</option>
      <option value="averagehelpfulscore_rf desc">Most Helpful</option>
      <option value="averageclarityscore_rf desc">Clearest</option>
      <option value="averageeasyscore_rf desc">Easiest</option>
      <option value="teacherlastname_sort_s asc">Alphabetical</option>
    </select></span>
  </div>
  <div class="professor-name-filter">
    <input id="professor-name" type="text" placeholder="Enter Your Professor's Name" value="" onfocus="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:SearchbynameSort', linkType:'o' } );">
  </div>
  <div class="filter-options">
    
      <a class="result" data-value="a" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">a</a>
    
      <a class="result" data-value="b" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">b</a>
    
      <a class="result" data-value="c" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">c</a>
    
      <a class="result" data-value="d" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">d</a>
    
      <a class="result" data-value="e" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">e</a>
    
      <a class="result" data-value="f" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">f</a>
    
      <a class="result" data-value="g" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">g</a>
    
      <a class="result" data-value="h" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">h</a>
    
      <a class="result" data-value="i" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">i</a>
    
      <a class="result" data-value="j" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">j</a>
    
      <a class="result" data-value="k" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">k</a>
    
      <a class="result" data-value="l" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">l</a>
    
      <a class="result" data-value="m" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">m</a>
    
      <a class="result" data-value="n" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">n</a>
    
      <a class="result" data-value="o" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">o</a>
    
      <a class="result" data-value="p" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">p</a>
    
      <a class="result" data-value="q" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">q</a>
    
      <a class="result" data-value="r" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">r</a>
    
      <a class="result" data-value="s" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">s</a>
    
      <a class="result" data-value="t" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">t</a>
    
      <a class="result" data-value="u" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">u</a>
    
      <a class="result" data-value="v" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">v</a>
    
      <a class="result" data-value="w" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">w</a>
    
      <a class="result" data-value="x" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">x</a>
    
      <a class="result" data-value="y" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">y</a>
    
      <a class="result" data-value="z" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AlphaFilter', linkType:'o' } );">z</a>
    
    <a class="result" data-value="All">All</a>
  </div>
</div>
<div class="result-list">
  <ul>
  <li>
    <a href="/ShowRatings.jsp?tid=39922">
      <span class="good-icon"></span>
      <span class="rating">4.4</span>
      <span class="name">Coppolino, Marc
        <span class="info">44 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=706863">
      <span class="average-icon"></span>
      <span class="rating">3.1</span>
      <span class="name">Gregory, T. Ryan
        <span class="info">39 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=316576">
      <span class="good-icon"></span>
      <span class="rating">3.7</span>
      <span class="name">Crawford, Steven
        <span class="info">36 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=53499">
      <span class="good-icon"></span>
      <span class="rating">4.1</span>
      <span class="name">Ferguson, Moira
        <span class="info">33 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=266451">
      <span class="average-icon"></span>
      <span class="rating">3.1</span>
      <span class="name">Bendall, Andrew
        <span class="info">30 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=91989">
      <span class="good-icon"></span>
      <span class="rating">3.6</span>
      <span class="name">Jadeski, Lorraine
        <span class="info">27 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=1762354">
      <span class="good-icon"></span>
      <span class="rating">3.6</span>
      <span class="name">Jacobs, Shoshanah
        <span class="info">21 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=146863">
      <span class="average-icon"></span>
      <span class="rating">3.1</span>
      <span class="name">Baker, Mark
        <span class="info">20 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=168534">
      <span class="average-icon"></span>
      <span class="rating">3.2</span>
      <span class="name">Bag, Jnanankur
        <span class="info">19 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=487688">
      <span class="good-icon"></span>
      <span class="rating">4.2</span>
      <span class="name">Dyck, David
        <span class="info">19 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=324342">
      <span class="average-icon"></span>
      <span class="rating">2.5</span>
      <span class="name">Watson, Alan
        <span class="info">17 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=797252">
      <span class="good-icon"></span>
      <span class="rating">4.4</span>
      <span class="name">Fudge, Douglas
        <span class="info">15 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=1267715">
      <span class="average-icon"></span>
      <span class="rating">2.7</span>
      <span class="name">Griswold, Cortland
        <span class="info">15 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=818929">
      <span class="good-icon"></span>
      <span class="rating">3.6</span>
      <span class="name">Cottenie, Karl
        <span class="info">12 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=21542">
      <span class="good-icon"></span>
      <span class="rating">3.7</span>
      <span class="name">Nassuth, Annette
        <span class="info">12 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=1411410">
      <span class="average-icon"></span>
      <span class="rating">3.3</span>
      <span class="name">Laberge, Fred
        <span class="info">11 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=461494">
      <span class="good-icon"></span>
      <span class="rating">4.2</span>
      <span class="name">Robinson, Beren
        <span class="info">10 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=178380">
      <span class="good-icon"></span>
      <span class="rating">4.1</span>
      <span class="name">Danzmann, Roy
        <span class="info">9 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=331404">
      <span class="good-icon"></span>
      <span class="rating">3.5</span>
      <span class="name">Mallard, Bonnie
        <span class="info">9 RATINGS</span>
      </span>
    </a>
  </li>

  <li>
    <a href="/ShowRatings.jsp?tid=803736">
      <span class="good-icon"></span>
      <span class="rating">3.8</span>
      <span class="name">Newman, Jonathan
        <span class="info">9 RATINGS</span>
      </span>
    </a>
  </li>
</ul>
  <div class="progressbtnwrap" data-search-type="search" style="display: block;">
    <div class="content" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:LoadMore', linkType:'o' } );">Load More</div>
    <div class="progress-bar"></div>
  </div>
</div>
<div class="add-professor">
  don't see your professor? <a href="/teacher/create" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROFMIDPANE:AddProf', linkType:'o' } );">add them.</a>
</div>

<script type="text/template" id="professor-result-template">
  <li>
    <a href="/ShowRatings.jsp?tid={{id}}">
      <span class="{{ratingclass}}-icon"></span>
      <span class="rating">{{overall_rating}}</span>
      <span class="name">{{plname}}, {{{pfname}}}
        <span class="info">{{rating_count}} RATINGS</span>
      </span>
    </a>
  </li>
</script>
<!--googleon: index-->
      </div>
    </div>
    <!-- Notes Template -->
    <script type="text/template" id="noteTemplate">
      <tr id="note-{{id}}">
        <td>
          <div class="posted">
            Posted on: {{dateCreated}} <br />
            Last Updated: {{lastUpdateDate}}
          </div>
        </td>
        <td class="class">
          <span class="name">{{className}}</span>
        </td>
        <td class="comments">
          <div class="read-mode">
            <p>
              {{comments}}
            </p>
            {{#if showEdit}}
              <div class="editLinks">
                <a href="javascript:void(0)" class="editNote" data-id={{id}} data-tid="1981141">Edit /</a>
                <a href="javascript:void(0)" class="deleteNote" data-id={{id}} data-tid="1981141">Delete</a>
              </div>
            {{/if}}
            
              <div class="helpful-links thumbs">
                <a href="#" class="helpful" data-url="/rmpRebuttal/updateRebuttalHelp/{{id}}" data-tid="1981141"><span >{{helpCount}}</span><span class="grouping">{{usefulGrouping}}</span> found this helpful</a>
                <a href="#" class="nothelpful" data-url="/rmpRebuttal/updateRebuttalHelp/{{id}}" data-tid="1981141"><span>{{notHelpCount}}</span> <span class="grouping">{{unUsefulGrouping}}</span> did not find his helpful</a>
              </div>
            
            <div class="helpful-links">
              <a href="/flagRebuttal.jsp?rebuttalId={{id}}&tid=1981141" class="report">report this note</a>
            </div>
          </div>
          {{#if showEdit}}
            <div class="edit-mode">
              <textarea class="edit-note-box">{{comments}}</textarea>
              <a href="javascript:void(0)" class="deleteNote">Delete This Comment</a>
              <a href="#" class="btn save-edit" data-id="{{id}}">Save</a>
            </div>
          {{/if}}
        </td>
      </tr>
    </script>
    <!-- Ends Notes Template -->
    <!-- Modals -->
    <!-- Starts Tags Modal -->
    <div id="chooseTagModal" class="reveal-modal">
      <form action="/AddRating.jsp?tid=1981141" method="post" name="chooseTagForm" id="chooseTagForm">
        <div class="modal-header">Tag your professor</div>
        <p>Select up to 3 tags that best describe your professor.</p>
        <div class="tag-holder">
          
            <a href="#" class="inactive">Tough Grader</a>
          
            <a href="#" class="inactive">Gives good feedback</a>
          
            <a href="#" class="inactive">Expect homework</a>
          
            <a href="#" class="inactive">Get ready to read</a>
          
            <a href="#" class="inactive">Gives Pop Quizzes</a>
          
            <a href="#" class="inactive">Participation matters</a>
          
            <a href="#" class="inactive">Skip class? You won't pass.</a>
          
            <a href="#" class="inactive">Respected by students</a>
          
            <a href="#" class="inactive">Inspirational</a>
          
            <a href="#" class="inactive">Lectures are long</a>
          
            <a href="#" class="inactive">Gives Extra Credit</a>
          
            <a href="#" class="inactive">Tests? Not many</a>
          
            <a href="#" class="inactive">Hilarious</a>
          
            <a href="#" class="inactive">Clear grading criteria</a>
          
            <a href="#" class="inactive">There for you</a>
          
            <a href="#" class="inactive">Assigns Long Papers</a>
          
            <a href="#" class="inactive">Amazing lectures</a>
          
            <a href="#" class="inactive">Tests are tough</a>
          
            <a href="#" class="inactive">Beware Of Group Projects</a>
          
            <a href="#" class="inactive">Would take again</a>
          
        </div>
        <input type="hidden" id="tags" name="chosen_tags">
        <input type="submit" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Tags_Continue', linkType:'o' } );this.style.display='none';" value="Continue" name="tagSubmit" id="tagSubmit">
      </form>
      <a class="close-reveal-modal" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROF:Tags_Cancel', linkType:'o' } );">×</a>
    </div>
    <!-- Ends Tags Modal -->
    <!-- Delete Note Modal -->
    <div id="deleteNoteModal" class="reveal-modal">
      <div class="delete-confirmed">
        <div class="modal-header">Your Note Has Been Deleted</div>
        <div class="delete-options">
          <a href="javascript:void(0)" class=" close-reveal-modal btn close-delete-confirm">Close</a>
        </div>
      </div>
      <div class="delete-not-confirmed">
        <div class="modal-header">Delete Note?</div>
        <div class="delete-text">Are you sure you want to delete this note? Once deleted, we can't bring it back.</div>
        <div class="delete-options">
          <a href="javascript:void(0)" class="delete-confirm" data-id="">Yes</a>
          <a href="javascript:void(0)" class="close-reveal-modal no">No</a>
        </div>
      </div>
      <a class="close-reveal-modal">×</a>
    </div>
    <!-- Delete Note Modal -->
    <!-- Save Note Modal -->
    <div id="saveNoteModal" class="reveal-modal">
      <div class="modal-header">Note Submitted</div>
      <p>Thank you for submitting your note.</p>
      <a href="javascript:void(0)" class="btn close-this save">Close</a>
      <a class="close-reveal-modal">×</a>
    </div>
    <!-- Save Note Modal -->
    <!-- Modals -->
    <!-- handlebar rating template -->
    <script type="text/template" id="ratingTemplate">
      <tr class = "{{class}}">
        <td class="rating">
          <div class="date">{{rDate}}</div>
          <div class="rating-block ">
            <div class="rating-wrapper">
              <div class="icon {{quality}}-icon"></div>
              <span class="rating-type">{{quality}}</span>
            </div>
            <div class="breakdown">
              <div class="break">
                <span class="score {{helpColor}}">{{rHelpful}}</span>
                <span class="descriptor">Helpfulness</span>
              </div>
              <div class="break">
                <span class="score {{clarityColor}}">{{rClarity}}</span>
                <span class="descriptor">Clarity</span>
              </div>
              <div class="break">
                <span class="score {{easyColor}}">{{rEasy}}</span>
                <span class="descriptor">Easiness</span>
              </div>
            </div>
          </div>
        </td>
        <td class="class">
          <span class="name {{onlineClass}}">{{rClass}}</span>
          <span class="credit">For Credit:{{takenForCredit}} </span>
          <span class="attendance">Attendance: {{attendance}}</span>
          <span class="textbook-use">Textbook Use: {{rTextBookUse}}</span>
          <span class="rater-interest">Rater Interest: {{rInterest}}</span>
          <span class="grade">Grade Received: {{teacherGrade}}</span>
        </td>
        <td class="comments" colspan="2">
          <div class="tagbox">
            {{#teacherRatingTags}}
              <span>{{this}}</span>
            {{/teacherRatingTags}}
          </div>
          <p>
            {{rComments}}
          </p>
          
            <div class="helpful-links thumbs">
              <a href="#" data-id="{{sId}}" class="helpful" data-url="/teacherRating/updateTeacherRatingHelp/{{id}}" data-tid="1981141"> <span class="count">{{helpCount}} </span> <span class="grouping">{{usefulGrouping}}</span> found this useful</a>
              <a href="#" data-id="{{sId}}" class="nothelpful" data-url="/teacherRating/updateTeacherRatingHelp/{{id}}" data-tid="1981141"> <span class="count">{{notHelpCount}}</span> <span class="grouping">{{unUsefulGrouping}}</span> did not find this useful</a>
            </div>
          
          <div class="helpful-links">
            <a href="/flagTeacherRating.jsp?rid={{id}}&tid=1981141" class="report" data-report-text="{{rComments}}">report this rating</a>
          </div>
        </td>
      </tr>
    </script>
  
        </div>
      </div>
      <!-- Ends Body Content -->

      <!-- Starts Mobile Footer -->
      
        

<footer class="mobileFooter hidden-lg">
  <ul>
    <li>
      <a href="/About.jsp">about</a>
    </li>
    <li>
      <a href="/mobile/blog" id="blogMobileFooterLink">blog</a>
    </li>
    <li>
      <a href="http://shop.mtv.com/category/79629920321/1/Rate-My-Professors.htm?utm_source=rmpcom&amp;utm_medium=topnav&amp;utm_campaign=rmpprods" target="_blank">Store</a>
    </li>
    <li>
      <a href="/help.jsp">Help</a>
    </li>
    <li>
      <a href="/utility/contact">Contact Us</a>
    </li>
    <li>
      <a href="http://srp.viacom.com/sitefaq.html" target="_blank">Ad Choices</a>
    </li>
    <li>
      <a href="/TermsOfUse_us.jsp#use" id="mobile_termUsePage">Terms &amp; Conditions <span class="m_last_modified">Last Modified (1/1/2015)</span></a>
    </li>
    <li>
      <a href="/TermsOfUse_us.jsp#privacy" id="mobile_privacyPage">Privacy Policy/Your CA Privacy Rights <span class="m_last_modified">Last Modified (1/1/2015)</span></a>
    </li>
    <li>
      <a href="/TermsOfUse_us.jsp#copyright" id="mobile_copyRightPage">Copyright Compliance Policy</a>
    </li>
    <li class="terms-conditions">
      ©2016 RateMyProfessors.com LLC. All Rights Reserved. Powerd by <a href="http://mtvu.com" target="_blank">mtvU</a>. mtvU is a trademark of Viacom International Inc.
    </li>
  </ul>
</footer>

      
      <!-- Ends Footer -->
    </div>
    <!-- Ends the page wrap -->

    <!-- Starts Desktop Footer -->
    
      


<footer class="mainFooter hidden-md">
  <ul id="leftFooter">
    <li><a href="/About.jsp">about</a> / </li>
    <li><a href="/blog/buzzpost/yoda-legendary-jedi-warrior/?all=1" id="blogFooterLink">blog</a> / </li>
    <li><a href="http://shop.mtv.com/category/79629920321/1/Rate-My-Professors.htm?utm_source=rmpcom&amp;utm_medium=topnav&amp;utm_campaign=rmpprods" target="_blank">Store</a> / </li>
    <li><a href="/help.jsp">Help</a> / </li>
    <li><a href="/utility/contact">Contact Us</a> / </li>
    <li><a href="http://srp.viacom.com/sitefaq.html" target="_blank">Ad Choices</a> / </li>
    <li><a href="/TermsOfUse_us.jsp#use" id="termUsePage">Terms &amp; Conditions <span class="last_modified">Last Modified (1/1/2015)</span></a> / </li>
    <li><a href="/TermsOfUse_us.jsp#privacy" id="privacyPage">Privacy Policy/Your ca privacy rights <span class="last_modified">Last Modified (1/1/2015)</span></a> / </li>
    <li><a href="/TermsOfUse_us.jsp#copyright" id="copyRightPage">Copyright Compliance Policy</a></li>
    
  </ul>
  <section class="copyright">
    ©2016 RateMyProfessors.com LLC. All Rights Reserved. Powered by <a href="http://mtvu.com" target="_blank">mtvU</a>. mtvU is a trademark of Viacom International Inc.
  </section>
</footer>

    
    <!-- Ends Footer -->

    <div class="promotion">
  <a class="open" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROMOS:Maximize', linkType:'o' } );">◀</a>
  <a class="close" onclick="javascript:mtvn.btg.Controller.sendLinkEvent({ linkName:'PROMOS:Minimize', linkType:'o' } );">×</a>
  <div class="content">
    <img class="promo-image" src="http://blog.ratemyprofessors.com/wp-content/uploads/2015/07/tumblr_logo_white_blue_128.png">
    <div class="text-content">
      <h3 class="title">We're on Tumblr!</h3>
      <span class="description">Follow Rate My Professors on Tumblr for feature updates, memes, giveaways and more.  </span>
    </div>
    <div class="clearfix"></div>
    <span id="promoid" style="display:none">17</span>
    <a class="more-info" onclick="promoClickEvent();" href="http://ratemyprofessors.tumblr.com/">Follow us now!</a>
  </div>
</div>

    <!-- Starts the student Drop down -->
<!-- Ends the student drop down -->

<!-- Starts the Professor Drop down -->
<!-- Ends the Professor Drop down -->


<!-- Starts the login menu -->
<!-- Starts the login Menu -->
<script type="text/template" id="loginTemplate">

  <div id="loginMenu" class="lform">
    <div class="header">
      Login to Rate My Professors
    </div>
    <div class="why-signup">
      <span>Go ahead, log in, you're still anonymous.</span> You're always anonymous here, but logging in will save your school and recent searches, helping you find professors faster. You can thank us later.
    </div>
    <form id="loginForm" action="/userauth" method="post">
      <div class="form-element">
        <div class="error email password">Incorrect email or password</div>
        <div class="label">email</div>
        <input type="text" name="pemail" class="pemail"/>
      </div>

      <div class="form-element">
        <div class="label">password</div>
        <input type="text" name="ppassword" class="ppassword" />
      </div>

      <div class="form-element">
        <input type="checkbox" name="remember" value="0"/>
        <label class="rememberme">Remember Me</label>
        <a href="#" class="forgotpw" id="forgotPassword">Forgot my password </a>
      </div>

      <div class="form-element">
        <input type="submit" id="userLogin" value="Login"/>
        <div class="or-block">
          <hr/>
          <div class="ortext">or</div>
        </div>
        <a href="#" id="signupLink">Sign up for an account</a>

      </div>

    </form>

  </div>

</script>

<!-- Ends: login menu -->
<!-- Ends the login menu -->

<!-- Starts the Forgotten Password fields -->
<!-- Starts Forgot Password fields -->
<script type="text/template" id="resetPasswordForm">

  <div id="resetPassword" class="lform">
    <div class="header">Forgot Password</div>
    <p>Enter your login email to reset your password.</p>
    <form action="" method="post" id="resetPasswordField">
      <div class="form-element email-form">
        <div class="label">email</div>
        <input type="text" name="reset_password" id="reset_password">
      </div>
      <div class="form-element">
        <input type="submit" value="Reset password" id="reset_password_submit">
      </div>
    </form>
  </div>

</script>

<!-- Ends Forgot Password fields -->
<!-- Ends the Forgotten Password fields-->

<!-- Starts the create a user drop down -->

<!-- Ends the create user drop down -->


<!-- Starts the main auto complete template -->
<script type="text/template" id="autocomplete-profitem">
  <li data-id="{{pk_id}}">
    <span class="wrap">
      <span class="main">{{{teacherfullname_s}}}</span>
      <span class="sub">{{schoolname_s}}</span>
    </span>
  </li>
</script>
<script type="text/template" id="autocomplete-schoolitem">
  <li data-id="{{pk_id}}">
    <span class="wrap">
      <span class="main">{{schoolname_s}}</span>
      <span class="sub">{{schoolcity_s}}, {{schoolstate_s}}  <span class="typeahead-country">{{schoolcountry_s}}</span></span>
    </span>
  </li>
</script>
<!-- Ends the main auto complete template -->

    <script type="text/javascript">
      window.RMP = window.RMP || {};
      window.RMP.Settings = {
        pathname : "",
        uri : "/ShowRatings.jsp",
        page: "show_professor",
        typeahead :"http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10",
        professorID : "1981141",
        schoolID: "",
        department: "Biology",
        state: "ON",
        country: "1",
        user: {},
        pageLevelData: {
  "pageName": "/professors/Alex Smith/1981141",
  "channel": "professors",
  "v49": "professors",
  "heir2": "/professors/Alex Smith/1981141",
  "prop2": "Canada",
  "prop3": "Biology",
  "prop5": "ON",
  "prop6": "University of Guelph",
  "prop7": "Alex Smith",
  "prop8": "visitor",
  "prop9": "1426",
  "prop10": "1981141",
  "section": "professors"
},
        reloadInterval: 60000
      }
    </script>
    <!-- Coda Implementation -->
    <script type="text/javascript">
      if (typeof MTVN == "undefined") MTVN = {};
      if (typeof MTVN.config == "undefined") MTVN.config = {};
      if (typeof MTVN.config.btg == "undefined") MTVN.config.btg = {};
      if (typeof MTVN.config.btg.DoubleClick == "undefined") MTVN.config.btg.DoubleClick = {};

      MTVN.config.btg.DoubleClick.auto = false;
      MTVN.config.btg.DoubleClick.onDemand = true;
      MTVN.config.btg.DoubleClick.reloadableAds = true;
      MTVN.config.btg.DoubleClick.reloadInterval = 60000;
      //temporary setting for testing refresh by visibility only on search page
      //if(RMP.Settings.page == 'show_school')
      //   var autoRefreshByVisibility = true;
      //else
        var autoRefreshByVisibility = false;
      console.log("Refresh By Visibility: " + (autoRefreshByVisibility ? 'On' : 'Off'))

      var vmn_page_data = {
        "metadata" :  { "property" : "rmp", "hub" : "", "is_main": false },
        "mappings" : {
          "ad-unit" : {"1" : "@property","2": "professor" },
          "key-values" : {
  "pageName": "/professors/Alex Smith/1981141",
  "channel": "professors",
  "v49": "professors",
  "heir2": "/professors/Alex Smith/1981141",
  "prop2": "Canada",
  "prop3": "Biology",
  "prop5": "ON",
  "prop6": "University of Guelph",
  "prop7": "Alex Smith",
  "prop8": "visitor",
  "prop9": "1426",
  "prop10": "1981141",
  "section": "professors"
},
          "exclusion-categories" : "hub_pages"
        },
        "settings" : {
          "reload" : true,
          "reload_interval": 60000,
          "autoRefreshByVisibility" : autoRefreshByVisibility
        }
      };
    </script>
    <script type="text/javascript" src="https://btg.mtvnservices.com/aria/coda.html?site=ratemyprofessors.com"></script>
    <script type="text/javascript" src="https://mediamtvnserv-a.akamaihd.net/player/api/2.11.7/api.min.js"></script>
    <script language="JavaScript" type="text/javascript">
   	  // This needs to be enabled in RMP's environment
      mtvn.btg.config.ReportSettings.Omniture={ enable:true, account:'viaviarmp', trackExternalLinks:true };
    </script>
    <!-- Coda Implementation -->

    <script src="/assets/application-7754889811077262e202d1e34d139109.js" type="text/javascript"></script><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-1" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-2" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-3" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-4" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-5" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-6" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-7" tabindex="0" style="z-index: 2; display: none;"></ul><ul class="ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-8" tabindex="0" style="z-index: 1; display: none;"></ul><ul class="typeahead typeahead-long dropdown-menu"></ul>
    <script src="/assets/libs/utils-2639ce16fb18c8e1581d3977fde5bfc9.js" type="text/javascript"></script>
  <!-- PAGEOK -->
  
<script id="hiddenlpsubmitdiv" style="display: none;"></script><script>try{(function() { for(var lastpass_iter=0; lastpass_iter < document.forms.length; lastpass_iter++){ var lastpass_f = document.forms[lastpass_iter]; if(typeof(lastpass_f.lpsubmitorig2)=="undefined"){ lastpass_f.lpsubmitorig2 = lastpass_f.submit; if (typeof(lastpass_f.lpsubmitorig2)=='object'){ continue;}lastpass_f.submit = function(){ var form=this; var customEvent = document.createEvent("Event"); customEvent.initEvent("lpCustomEvent", true, true); var d = document.getElementById("hiddenlpsubmitdiv"); if (d) {for(var i = 0; i < document.forms.length; i++){ if(document.forms[i]==form){ if (typeof(d.innerText) != 'undefined') { d.innerText=i.toString(); } else { d.textContent=i.toString(); } } } d.dispatchEvent(customEvent); }form.lpsubmitorig2(); } } }})()}catch(e){}</script></body></html>'''

soup = BeautifulSoup(html_doc, 'html.parser')

if soup.find(class_="headline") == None:
	print "empty"

