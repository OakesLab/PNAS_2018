





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-PkbtxdWDpLChpxtWQ0KbvJoef4XMYPq5pfd/ZmylYZTzXYpCfGwN9d+bsSKcmOJLwTkfjFkfj5wz3poDrhJoSQ==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-f6e6ce21346c0d2eb22def1e8534afcb.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-XiPiEdaRO+K7+Dt5NlEkDnTWKY8GSgW4wfgvr7YV6lZiHHpjOoAnKtuK3G4y8mRnxQ4ieaEWw6ZDa2UMQHLyxQ==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-6aa762e23e9f19a4f9dd2eec1573d451.css" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>Oakes-Lab-Notebook/lamellipodium_plotter.py at master · askeeters/Oakes-Lab-Notebook</title>
    <meta name="description" content="GitHub is where people build software. More than 28 million people use GitHub to discover, fork, and contribute to over 85 million projects.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/24983430?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="askeeters/Oakes-Lab-Notebook" /><meta property="og:url" content="https://github.com/askeeters/Oakes-Lab-Notebook" /><meta property="og:description" content="Oakes-Lab-Notebook - Static website content for my lab notebook, published with Org Mode" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6Mjg1MjczMjQ0OjA5NTU0NmM0ODk2NzUzZDY4MGY2YzdmM2IyYzU3MTIxY2NjODI0MGI5ZWQxMjYyNTcxMmYwNTQzMDgzMTZlZmY=--a1dee39df73a5934228f3626aed0367baa834361">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="EF4B:212F:35EAE6D:62C3ADC:5B1DC19F" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="EF4B:212F:35EAE6D:62C3ADC:5B1DC19F" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="30160078" /><meta name="octolytics-actor-login" content="OakesLab" /><meta name="octolytics-actor-hash" content="fe89fe71a2aa24711f37c96fb08bcfc10cd4451dd3fcaf879a24c8b54de3b54b" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="OakesLab">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="YmUzM2EzNjc5ZjI4NGNiZmY0M2E5ODg0NzMwZDY3ODllYzgyZWExYzJlZDA0YWU0MjY2NWJkZDcyMDliYzJkYnx7InJlbW90ZV9hZGRyZXNzIjoiNzQuNjkuOTAuMjEyIiwicmVxdWVzdF9pZCI6IkVGNEI6MjEyRjozNUVBRTZEOjYyQzNBREM6NUIxREMxOUYiLCJ0aW1lc3RhbXAiOjE1Mjg2NzY4MTMsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS,MARKETPLACE_INSIGHTS,MARKETPLACE_INSIGHTS_CONVERSION_PERCENTAGES">

  <meta name="html-safe-nonce" content="aa7f0f205380903b50df586ad140b0c94f3ab8b0">

  <meta http-equiv="x-pjax-version" content="8b6ccf2fb8fe60e9e375f7236dedc16a">
  

      <link href="https://github.com/askeeters/Oakes-Lab-Notebook/commits/master.atom" rel="alternate" title="Recent Commits to Oakes-Lab-Notebook:master" type="application/atom+xml">

  <meta name="description" content="Oakes-Lab-Notebook - Static website content for my lab notebook, published with Org Mode">
  <meta name="go-import" content="github.com/askeeters/Oakes-Lab-Notebook git https://github.com/askeeters/Oakes-Lab-Notebook.git">

  <meta name="octolytics-dimension-user_id" content="24983430" /><meta name="octolytics-dimension-user_login" content="askeeters" /><meta name="octolytics-dimension-repository_id" content="90157716" /><meta name="octolytics-dimension-repository_nwo" content="askeeters/Oakes-Lab-Notebook" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="90157716" /><meta name="octolytics-dimension-repository_network_root_nwo" content="askeeters/Oakes-Lab-Notebook" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/askeeters/Oakes-Lab-Notebook/blob/master/code/lamellipodium_plotter.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

<link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 container-lg">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search position-relative" role="search">
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="90157716" data-scoped-search-url="/askeeters/Oakes-Lab-Notebook/search" data-unscoped-search-url="/search" action="/askeeters/Oakes-Lab-Notebook/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          aria-label="Search this repository"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=0XAUR0pc2K71VthgFo/XTycgF188OFmLrAZj3CquxsNmS8gvv++2U2lYPqXEGR6+PGXKJ92b+BTcVR0NfnWEYg=="
          spellcheck="false"
          autocomplete="off"
          autocapitalize="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://assets-cdn.github.com/images/search-shortcut-hint.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              <ul class="d-none js-jump-to-suggestions-template-container">
                <li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item">
                  <a class="no-underline d-flex flex-auto flex-items-center p-2 jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open" aria-label="Jump to..." href="">
                    <div class="jump-to-octicon js-jump-to-octicon mr-2 text-center d-none"></div>
                    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar" alt="" src="" width="28" height="28">
                    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden no-wrap css-truncate css-truncate-target">
                    </div>

                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-search">
                      In this repository
                      <span class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>

                    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
                      Jump to
                      <span class="d-inline-block ml-1 v-align-middle">↵</span>
                    </div>
                  </a>
                </li>
                <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-repo-octicon-template" title="Repository" viewBox="0 0 12 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
                <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-project-octicon-template" title="Project" viewBox="0 0 15 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
                <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-search-octicon-template" title="Search" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
              </ul>
              <ul class="d-none js-jump-to-no-results-template-container">
                <li class="d-flex flex-justify-center flex-items-center p-3 f5 d-none">
                  <span class="text-gray">No suggested jump to results</span>
                </li> 
              </ul>

              <ul class="js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
                <li class="d-flex flex-justify-center flex-items-center p-0 f5">
                  <img src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
                </li>
              </ul>
            </div>
      </label>
</form>  </div>
</div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
                <li>
                  <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar, group:" data-selected-links=" /marketplace" href="/marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:30160078" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.99 11.991v1H0v-1l.73-.58c.769-.769.809-2.547 1.189-4.416.77-3.767 4.077-4.996 4.077-4.996 0-.55.45-1 .999-1 .55 0 1 .45 1 1 0 0 3.387 1.229 4.156 4.996.38 1.879.42 3.657 1.19 4.417l.659.58h-.01zM6.995 15.99c1.11 0 1.999-.89 1.999-1.999H4.996c0 1.11.89 1.999 1.999 1.999z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown">
    <details class="details-expanded details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="askeeters/Oakes-Lab-Notebook">This repository</span>
  </div>
    <a class="dropdown-item" href="/askeeters/Oakes-Lab-Notebook/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown">

    <details class="details-expanded details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@OakesLab" class="avatar float-left mr-1" src="https://avatars0.githubusercontent.com/u/30160078?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">OakesLab</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/OakesLab" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/OakesLab?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="2x9mlKBIcYAEHJirG+rVuZHU/x60P7aGjWftFSrzosQfINQq5nbbJynaudXmdOv/0dV8K6IkRHkXgq6czFf9YQ==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="byhZqxHJ+/OyvtoADt2hTg+YFgf2a/eVOZMIWkx3S3mrF+sVV/dRVJ94+37zQ58IT5mVMuBwBWqjdkvTqtMU3A==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      







  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="kAWaZc6WS7EOHk60HXO30s2Ty8e3Eo9XQJ976fOHABf3ZU6YhlBjw47IQr/jWhgrc9mrdk+Ztkh1LAY2Dzf5+w==" />      <input type="hidden" name="repository_id" id="repository_id" value="90157716" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/askeeters/Oakes-Lab-Notebook/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/askeeters/Oakes-Lab-Notebook/watchers"
            aria-label="0 users are watching this repository">
            0
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" checked="checked" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/askeeters/Oakes-Lab-Notebook/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="b6hZMCDhYykq7CmbswALXP9z/wKaUNZc4BMI6AZK2gOoFm3OyCX3UTcZLGLJ1Us8cBSoIHmsBLpEsg0Of4+sZw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar askeeters/Oakes-Lab-Notebook"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/askeeters/Oakes-Lab-Notebook/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/askeeters/Oakes-Lab-Notebook/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="ZxJkt5lKLMlKeGIgqh/xOlEw/ywMzAnr5YyvzjjZ5ILjRdTiXYgGqzPkEJfX7QL0TJUtXmjpVeY/QeMhYk5kDQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star askeeters/Oakes-Lab-Notebook"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/askeeters/Oakes-Lab-Notebook/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/askeeters/Oakes-Lab-Notebook/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="AmmYSrl8lquhdiMuq5zsBUu0na0aCVjEX9gfWMR1OFJ7axhqSTpA1mpB6aAPIIKBuJx6ojsqRcMkTy7QfUQ7uA==" />
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of askeeters/Oakes-Lab-Notebook to your account"
                aria-label="Fork your own copy of askeeters/Oakes-Lab-Notebook to your account">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/askeeters/Oakes-Lab-Notebook/network" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/askeeters">askeeters</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/askeeters/Oakes-Lab-Notebook">Oakes-Lab-Notebook</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /askeeters/Oakes-Lab-Notebook" href="/askeeters/Oakes-Lab-Notebook">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /askeeters/Oakes-Lab-Notebook/issues" href="/askeeters/Oakes-Lab-Notebook/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /askeeters/Oakes-Lab-Notebook/pulls" href="/askeeters/Oakes-Lab-Notebook/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /askeeters/Oakes-Lab-Notebook/projects" href="/askeeters/Oakes-Lab-Notebook/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /askeeters/Oakes-Lab-Notebook/wiki" href="/askeeters/Oakes-Lab-Notebook/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /askeeters/Oakes-Lab-Notebook/pulse" href="/askeeters/Oakes-Lab-Notebook/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/askeeters/Oakes-Lab-Notebook/blob/835fc90a9f2c18c702fd0c91743b3bdc7f31e493/code/lamellipodium_plotter.py">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:87a74c1c434adb9b70e1955572d25773 -->

  <div class="file-navigation">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/askeeters/Oakes-Lab-Notebook/blob/master/code/lamellipodium_plotter.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/askeeters/Oakes-Lab-Notebook/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
        Copy path
      </clipboard-copy>
    </div>
    <div id="blob-path" class="breadcrumb">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/askeeters/Oakes-Lab-Notebook"><span>Oakes-Lab-Notebook</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/askeeters/Oakes-Lab-Notebook/tree/master/code"><span>code</span></a></span><span class="separator">/</span><strong class="final-path">lamellipodium_plotter.py</strong>
    </div>
  </div>


  <include-fragment src="/askeeters/Oakes-Lab-Notebook/contributors/master/code/lamellipodium_plotter.py" class="commit-tease">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/askeeters/Oakes-Lab-Notebook/raw/master/code/lamellipodium_plotter.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/askeeters/Oakes-Lab-Notebook/blame/master/code/lamellipodium_plotter.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/askeeters/Oakes-Lab-Notebook/commits/master/code/lamellipodium_plotter.py">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/askeeters/Oakes-Lab-Notebook/edit/master/code/lamellipodium_plotter.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="U7UUiz7TScmHa6VnAO1IHnvetjnj/Z3WlqDu1mOJWWcd0B4a+rAU8uSuVw7gzHFqKobeO6gfKsdsMGVRCnvZuw==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/askeeters/Oakes-Lab-Notebook/delete/master/code/lamellipodium_plotter.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="5Na4bTInAq1tgTsYPSuD0KNdZ8TWHmibv54JUnU0ZOciP5io6thtgOuoxH6CJnWIJKHPY3MTNyaW92uCIhQ2pw==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      118 lines (98 sloc)
      <span class="file-info-divider"></span>
    6.25 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> matplotlib.pyplot <span class="pl-k">as</span> plt</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> pandas <span class="pl-k">as</span> pd</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> seaborn <span class="pl-k">as</span> sns</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numpy <span class="pl-k">as</span> np</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">sns.set_style(<span class="pl-s"><span class="pl-pds">&#39;</span>ticks<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">sns.set_palette(<span class="pl-s"><span class="pl-pds">&#39;</span>colorblind<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">data_path <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>c:/Users/avs11/Dropbox/SoftStiff Data/FA analysis/Analysis Data/Peak Positions/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">scan_path <span class="pl-k">=</span> <span class="pl-sr"><span class="pl-k">r</span><span class="pl-pds">&#39;</span>c:/Users/avs11/Dropbox/SoftStiff Data/FA analysis/Analysis Data/Band Scans/<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">color<span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>slategrey<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">soft_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_Peaks.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">soft_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>soft_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">stiff_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_Peaks.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">stiff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>stiff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">peaks <span class="pl-k">=</span> pd.concat([soft_peaks, stiff_peaks], <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">peaks <span class="pl-k">=</span> pd.melt(peaks, <span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, [<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>], <span class="pl-v">var_name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value_name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Peak_Depth<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">peaks.reindex()</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">soft_avg_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_Avg_Peaks.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">soft_avg_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>soft<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>soft_avg_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">stiff_avg_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_Avg_Peaks.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">stiff_avg_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>stiff<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>stiff_avg_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">avg_peaks <span class="pl-k">=</span> pd.concat([soft_avg_peaks, stiff_avg_peaks])</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">avg_peaks <span class="pl-k">=</span> pd.melt(avg_peaks, <span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, [<span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>], <span class="pl-v">var_name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">value_name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Peak_Depth<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">avg_peaks.reindex()</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">soft_diff_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_Pax_Min_P34.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">soft_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>soft_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">stiff_diff_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_Pax_Min_P34.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">stiff_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>stiff_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">diff_peaks <span class="pl-k">=</span> pd.concat([soft_diff_peaks, stiff_diff_peaks])</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">soft_avg_diff_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_Avg_Pax_Min_Avg_P34.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">soft_avg_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>soft_avg_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">stiff_avg_diff_peaks <span class="pl-k">=</span> pd.read_csv(data_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_Avg_Pax_Min_Avg_P34.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">stiff_avg_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>]<span class="pl-k">*</span>stiff_avg_diff_peaks[<span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>].count()</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">avg_diff_peaks <span class="pl-k">=</span> pd.concat([soft_avg_diff_peaks, stiff_avg_diff_peaks])</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plot the individual peaks relative to the actin &#39;zero&#39;</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">peaks_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">peaks_ax <span class="pl-k">=</span> peaks_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">sns.boxplot(<span class="pl-v">data</span><span class="pl-k">=</span>peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Peak_Depth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">hue</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>peaks_ax, <span class="pl-v">color</span><span class="pl-k">=</span>color, <span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">sns.stripplot(<span class="pl-v">data</span><span class="pl-k">=</span>peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Peak_Depth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">hue</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>peaks_ax, <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>, <span class="pl-v">split</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">handles, labels <span class="pl-k">=</span> plt.gca().get_legend_handles_labels()</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">plt.legend(handles[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>], labels[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>])</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">peaks_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth ($\mu \mathdefault<span class="pl-c1">{m}</span>$)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">peaks_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate Stiffness<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Box_Peaks_Jitter.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plot the average peaks relative to the actin &#39;zero&#39;</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">avg_peaks_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">avg_peaks_ax <span class="pl-k">=</span> avg_peaks_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">sns.boxplot(<span class="pl-v">data</span><span class="pl-k">=</span>avg_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Peak_Depth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">hue</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>avg_peaks_ax, <span class="pl-v">color</span><span class="pl-k">=</span>color, <span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">sns.stripplot(<span class="pl-v">data</span><span class="pl-k">=</span>avg_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Peak_Depth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">hue</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stain<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>avg_peaks_ax, <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span>, <span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>, <span class="pl-v">split</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">handles, labels <span class="pl-k">=</span> plt.gca().get_legend_handles_labels()</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">plt.legend(handles[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>], labels[<span class="pl-c1">0</span>:<span class="pl-c1">2</span>])</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">avg_peaks_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Average Peak Depth ($\mu \mathdefault<span class="pl-c1">{m}</span>$)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">avg_peaks_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate Stiffness<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Box_Avg_Peaks_Jitter.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plot the Pax-p34</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">diff_peaks_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">diff_peaks_ax <span class="pl-k">=</span> diff_peaks_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">sns.boxplot(<span class="pl-v">data</span><span class="pl-k">=</span>diff_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>diff_peaks_ax, <span class="pl-v">order</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>], <span class="pl-v">color</span><span class="pl-k">=</span>color ,<span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">sns.stripplot(<span class="pl-v">data</span><span class="pl-k">=</span>diff_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Pax-P34<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>diff_peaks_ax, <span class="pl-v">order</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>], <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span> ,<span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">diff_peaks_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate Stiffness<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">diff_peaks_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>$\mathdefault<span class="pl-c1">{x}</span>_\mathdefault<span class="pl-c1">{Pax}</span>-\mathdefault<span class="pl-c1">{x}</span>_\mathdefault<span class="pl-c1">{P34}</span>$<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Box_Diff_Peaks_Jitter.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plot the avg Pax- avg p34</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">avg_diff_peaks_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">avg_diff_peaks_ax <span class="pl-k">=</span> avg_diff_peaks_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">sns.boxplot(<span class="pl-v">data</span><span class="pl-k">=</span>avg_diff_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>avg_diff_peaks_ax, <span class="pl-v">order</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>], <span class="pl-v">color</span><span class="pl-k">=</span>color ,<span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">sns.stripplot(<span class="pl-v">data</span><span class="pl-k">=</span>avg_diff_peaks, <span class="pl-v">x</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Substrate<span class="pl-pds">&#39;</span></span>, <span class="pl-v">y</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Avg_Pax-P34<span class="pl-pds">&#39;</span></span>, <span class="pl-v">ax</span><span class="pl-k">=</span>avg_diff_peaks_ax, <span class="pl-v">order</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>], <span class="pl-v">color</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>k<span class="pl-pds">&#39;</span></span> ,<span class="pl-v">orient</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>v<span class="pl-pds">&#39;</span></span>, <span class="pl-v">alpha</span><span class="pl-k">=</span><span class="pl-c1">0.5</span>)</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">avg_diff_peaks_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Substrate Stiffness<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">avg_diff_peaks_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>$\overline{\mathdefault{x}_\mathdefault{Pax}}-\overline{\mathdefault{x}_\mathdefault{P34}}$<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Box_Avg_Diff_Peaks_Jitter.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Plot the linescans for the two cells that we chose</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">soft_p34 <span class="pl-k">=</span> pd.read_csv(scan_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_19_P34_prot_0.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">soft_pax <span class="pl-k">=</span> pd.read_csv(scan_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Soft_19_Paxillin_prot_0.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">stiff_p34 <span class="pl-k">=</span> pd.read_csv(scan_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_3_P34_prot_3.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">stiff_pax <span class="pl-k">=</span> pd.read_csv(scan_path<span class="pl-k">+</span><span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_3_Paxillin_prot_3.csv<span class="pl-pds">&#39;</span></span>,<span class="pl-v">header</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">names</span><span class="pl-k">=</span>[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>,<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">stiff_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">stiff_ax <span class="pl-k">=</span> stiff_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">stiff_ax.plot(stiff_p34[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>], stiff_p34[<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>o-<span class="pl-pds">&#39;</span></span>, <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">stiff_ax.plot(stiff_pax[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>], stiff_pax[<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>o-<span class="pl-pds">&#39;</span></span>, <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> sns.pointplot(data=stiff_p34, x=&#39;Peak Depth&#39;, y=&#39;Normalized Intensity&#39;, ax=stiff_ax, color=color)</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">stiff_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth ($\mu \mathdefault<span class="pl-c1">{m}</span>$)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">stiff_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">stiff_fig.suptitle(<span class="pl-s"><span class="pl-pds">&#39;</span>48 kPa<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">plt.ylim(<span class="pl-c1">0</span>, <span class="pl-c1">1.1</span>)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">plt.legend(<span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>best<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Stiff_Scan.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">soft_fig <span class="pl-k">=</span> plt.figure()</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">soft_ax <span class="pl-k">=</span> soft_fig.add_subplot(<span class="pl-c1">111</span>)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">soft_ax.plot(soft_p34[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>], soft_p34[<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>o-<span class="pl-pds">&#39;</span></span>, <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>P34<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">soft_ax.plot(soft_pax[<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth<span class="pl-pds">&#39;</span></span>], soft_pax[<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span>o-<span class="pl-pds">&#39;</span></span>, <span class="pl-v">label</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Paxillin<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> sns.pointplot(data=soft_p34, x=&#39;Peak Depth&#39;, y=&#39;Normalized Intensity&#39;, ax=soft_ax, color=color)</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">soft_ax.set_xlabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Peak Depth ($\mu \mathdefault<span class="pl-c1">{m}</span>$)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">soft_ax.set_ylabel(<span class="pl-s"><span class="pl-pds">&#39;</span>Normalized Intensity<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">soft_fig.suptitle(<span class="pl-s"><span class="pl-pds">&#39;</span>2.1 kPa<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">plt.ylim(<span class="pl-c1">0</span>, <span class="pl-c1">1.1</span>)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">plt.legend(<span class="pl-v">loc</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>best<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">plt.savefig(<span class="pl-s"><span class="pl-pds">&#39;</span>Soft_Scan.svg<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">plt.show()</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">exit</span>()</td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" href="/askeeters/Oakes-Lab-Notebook/blame/835fc90a9f2c18c702fd0c91743b3bdc7f31e493/code/lamellipodium_plotter.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" href="/askeeters/Oakes-Lab-Notebook/issues/new">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.25192s from unicorn-667f5bb658-nkplt">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-A0o32UigVgm0vxC5rUiim8r+tiSbIUPgybIJ76dL835MEyecNQOOkZ08YPRdpcPQWrF7k2apKd6gVtNmP0fbeg==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-9892af3afe548c0749013c43e335ae31.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-GwXdJGfmE4Y7zwaQcLCiC/XjFA9h8sBysvwAmFyP4EEez2tWJhjSqJNRNQCEQZDaBCM8MbJ4J/zxtuE/2DG2WQ==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-bcc5d59bbfe92b3354a32701be238fb9.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
  </div>
</div>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

