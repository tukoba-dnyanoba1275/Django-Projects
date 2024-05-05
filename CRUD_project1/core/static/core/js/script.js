//* selectors
const body = document.querySelector('body')
const themeChangeBtn = document.querySelector('#theme-Btn')



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



//* events
themeChangeBtn.addEventListener('click', handleThemeToggle)