var session = require('express-session')
const model = require("./model")

const register = (req, res) => {
    console.log(`registering in, body={userName:${req.body.userName}, userPassword:${req.body.userPassword}}`);
    const { userName, userPassword } = req.body;
    if (userName && userPassword) {
        model.count({ where: { userName } }).then(
            (count) => {
                if (count !== 0) {
                    res.send({ register: false });
                } else {
                    model.create({ userName, userPassword })
                        .then(() => res.send({ register: true }))
                        .catch((err) => {
                            res.send({ register: false });
                            console.log(err);
                        });
                }
            },
        );
    } else {
        res.send({ register: false });
    }
}

const login = (req, res) => {
    console.log(`logging in, body=${req.body}`);
    const { userName, userPassword } = req.body;

    if (!userPassword || !userName) {
        req.session.loggedin = false;
        res.send({ loggedin: req.session.loggedin });
        return;
    }
    const user = model.findOne({ where: { userName, userPassword } });
    if (!user) return;

    req.session.loggedin = true;
    res.send({ loggedin: req.session.loggedin });
}

const checkSessions = (req, res, next) => {
    if (req.session.loggedin) {
        next();
    } else {
        res.send({ loggedin: false });
    }
}

const loginTest = (req, res) => {
    res.send({ loggedin: true });
}

const logout = (req, res) => {
    console.log(`logging out, body=${req.body}`);

    req.session.destroy()
    res.send({ loggedin: false });
}

const getUsers = (req, res) => {
    model.findAll()
        .then((users) => res.send(users))
        .catch(e => console.log(e));
}

const getUser = (req, res) => {
    model.findByPk(req.params.id).then((users) => res.json(users)).catch(e => console.log(e));
}

const deleteUser = (req, res) => {
    model.destroy({ where: { id: req.params.id } }).then((r) => res.json(r).catch(e => console.log(e)));
}

module.exports = {register, login, checkSessions, loginTest, logout, getUsers, getUser, deleteUser}