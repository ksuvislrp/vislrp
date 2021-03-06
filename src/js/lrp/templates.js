// Load LRP template
export default function(template) {
    return JSON.parse(JSON.stringify(templates[template]));
}

var templates =  {
    'default': {
        id: 0,
        'method': ['customize'],
        'x0': 1,
        'x1': 39,
        'theta0': 1,
        'theta1': 1,
        'gamma0': 1,
        'gamma1': 1,
        'gamma1p': 1,
        'gamma1n': 1,
        'gamma2': 1,
        'eps': 1,
        'alpha': 1,
        'beta': 1,
    },
    '0': {
        id: 0,
        'method': ['0'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 1,
        'gamma1p': 0,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    },
    'epsilon': {
        id: 0,
        'method': ['epsilon'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 1,
        'gamma1p': 0,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0.25,
        'alpha': 1,
        'beta': 0,
    },
    'gamma': {
        id: 0,
        'method': ['gamma'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 1,
        'gamma1p': 0.3,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    },
    'alpha-beta': {
        id: 0,
        'method': ['alpha-beta'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 0,
        'gamma1p': 1,
        'gamma1n': 1,
        'gamma2': 0,
        'eps': 0,
        'alpha': 2,
        'beta': 1,
    },
    'alpha1-beta0': {
        id: 0,
        'method': ['alpha1-beta0'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 0,
        'gamma1p': 1,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    },
    'w_square': {
        id: 0,
        'method': ['w_square'],
        'x0': 1,
        'x1': 39,
        'theta0': 1,
        'theta1': 0,
        'gamma0': 0,
        'gamma1': 0,
        'gamma1p': 0,
        'gamma1n': 0,
        'gamma2': 1,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    },
    'flat': {
        id: 0,
        'method': ['flat'],
        'x0': 1,
        'x1': 39,
        'theta0': 1,
        'theta1': 0,
        'gamma0': 1,
        'gamma1': 0,
        'gamma1p': 0,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    },
    'z-beta': {
        id: 0,
        'method': ['z-beta'],
        'x0': 1,
        'x1': 39,
        'theta0': 0,
        'theta1': 1,
        'gamma0': 0,
        'gamma1': 0,
        'gamma1p': 0,
        'gamma1n': 0,
        'gamma2': 0,
        'eps': 0,
        'alpha': 1,
        'beta': 0,
    }
}