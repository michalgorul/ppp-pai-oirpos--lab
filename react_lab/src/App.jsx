import './App.css';
// Router imports
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
// Components
import Toolbar from './components/Toolbar';
// Pages
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import UserListPage from './pages/UserListPage';
import Chat from './pages/Chat.jsx';

function App() {
  return (
    <div>
      <Router>
        <Toolbar />
        <Switch>
          <Route path='/register' component={RegisterPage} />
          <Route path='/login' component={LoginPage} />
          <Route path='/chat' component={Chat} />
          {/* TODO: Route dla Chat.jsx */}
          {/* Default route */}
          <Route exact path='/'>
            <UserListPage />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
