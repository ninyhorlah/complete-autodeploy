import LoginUser from '../Pages/Login';
import SignUp from '../Pages/Signup';
import FirstStepPage from '../Pages/Dashboard';
import OnboardingPage from '../Pages/Onboarding';

// Config/routes.js

const routes = [
    {
      path:'/login',
      component: LoginUser,
      isPrivate: false
    },
    {
      path:'/dashboard',
      component: FirstStepPage,
      isPrivate: true
    },
    {
      path:'/signup',
      component: SignUp,
      isPrivate: false
    },
    {
      path:'/on',
      component: OnboardingPage
    },
]

export default routes