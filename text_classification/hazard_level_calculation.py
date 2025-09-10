def hazard_level_calculation(score):
    if score >= 0.5:
        return 'high'
    elif score >= 0.3:
        return 'medium'
    else:
        return  'none'