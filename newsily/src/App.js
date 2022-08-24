import React from 'react';
import { 
    BrowserRouter as Router,
    Switch
  } from 'react-router-dom';
import routes from './Config/routes.js';
import AppRoutes from './Components/AppRoute';
import { AuthProvider } from './Context'
import './App.css';

function App () {

  // const[onBoarding, setOnBoarding] = useState(true);
  // const[userData, setUserData] = useState({
  //   token : undefined,
  //   user : undefined
  // });
  // // const [isLogged, setLogin] = useState(null);
  // // const [user, setUser] = useState(null);
  // const [login, setLogin] = useState(false)
  // const [email, setEmail] = useState('');

  // const history = useHistory();
  
  // useEffect( () => {
  //   setTimeout( () => {
  //     setOnBoarding(false)
  //   }, 2000)
  // })

  // useEffect(() => {

  //   if (localStorage.getItem('token')) {
  //     Axios.get('http://localhost:8000/accounts/login/', {
  //       headers: {
  //         Authorization: `JWT ${localStorage.getItem('token')}`
  //       } 
  //     })
  //   } else {
  //     history.push('/signup')
  //   }  

  // });
  
  return (
    <AuthProvider>
			<Router>
				<Switch>
					{routes.map((route) => (
						<AppRoutes
							key={route.path}
							path={route.path}
							component={route.component}
							isPrivate={route.isPrivate}
						/>
					))}
				</Switch>
			</Router>
		</AuthProvider>
  );
}

export default App;
   