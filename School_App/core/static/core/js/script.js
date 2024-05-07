//* selectors
const body = document.querySelector('body')
const themeChangeBtn = document.querySelector('#theme-Btn')
const profileLogo = document.querySelector('.profile-logo')
const logoutBtnWrapper = document.querySelector('#logout-button-wrapper')
// console.log(logoutBtnWrapper);
// console.log(profileLogo);



//* state
const theme = localStorage.getItem('theme')



//* on mount 
theme && body.classList.add(theme) 
theme && (themeChangeBtn.textContent = '🔆')



//* handles
const handleThemeToggle = (event)=>{
  // console.log(event);
  body.classList.toggle('theme-dark')
  if (body.classList.contains('theme-dark')) {
    themeChangeBtn.textContent = '🔆'
    localStorage.setItem('theme', 'theme-dark')
  }
  else {
    themeChangeBtn.textContent = '🌙'
    localStorage.removeItem('theme')
  }
}
let toggle = true
const handleProfileLogoToggle = (e) => {
  // console.log(e);
  if (toggle) {
    logoutBtnWrapper.style.display = 'block'
    toggle = false
  }
  else {
    logoutBtnWrapper.style.display = 'none'
    toggle = true
  }
}


//* events
themeChangeBtn.addEventListener('click', handleThemeToggle)

profileLogo.addEventListener('click', handleProfileLogoToggle, false)