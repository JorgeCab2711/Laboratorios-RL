def update_estimates(arm, reward):
    pulled_arms = [0] * 10
    reward_estimates = [1] * 10
    pulled_arms[arm] = 2
    # aumentar el conteo del brazo seleccionado
    pulled_arms[arm] += 1

    
    reward_estimates[arm] = 6
    Q_t_a = reward_estimates[arm]


    reward_estimates[arm] = reward_estimates[arm] + ((1/pulled_arms[arm]) * (reward - Q_t_a))

    print(pulled_arms)
    print(reward_estimates)
    

update_estimates(1, 5.2)
