import { useEffect } from "react";
import "./App.css";
// Router imports
import { HashRouter as Router, Switch, Route } from "react-router-dom";
// Components
import Toolbar from "./components/Toolbar";
// Pages
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import UserListPage from "./pages/UserListPage";

function App() {
  return (
    <div>
      <Router>
        <Toolbar />
        <Switch>
          <Route path="/register" component={RegisterPage} />
          <Route path="/login" component={LoginPage} />
          {/* TODO: Route dla Chat.jsx */}
          {/* Default route */}
          <Route exact path="/">
            <UserListPage />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
