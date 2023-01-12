import Vue from "vue";
import Router from "vue-router";
import HomePage from "@/pages/HomePage";
import SearchPage from "@/pages/SearchPage";
import LoginPage from "@/pages/LoginPage";
import CallBack from "@/components/CallBack";
import UserAuth from "@/components/UserAuth";

Vue.use(Router)



export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            name: "Login",
            component: LoginPage
        },
         {
            path: "/callback",
            name: "callback",
            component: CallBack
        },

        {
            path:"/home",
            name: "home",
            component: HomePage,
        },

        {
            path: "/search",
            name: "search",
            component: SearchPage
        },

        {
            path: "/auth",
            name: "userAuth",
            component: UserAuth
        }
    ]
})