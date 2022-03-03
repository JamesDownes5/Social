const signup = Vue.createApp({
    data() {
        return{
            logo: {% static 'core/logo.png' %},
        }
    }
})

signup.mount('#SignUp')
