export const ROUTES = {
  // Public routes
  HOME: '/',
  LOGIN: '/login',
  SIGNUP: '/signup',
  FORGOT_PASSWORD: '/forgot-password',
  RESET_PASSWORD: '/reset-password',

  // App routes (authenticated)
  DASHBOARD: '/dashboard',

  // Tournament routes
  TOURNAMENTS: '/tournaments',
  TOURNAMENT_DETAILS: (id: string | number) => `/tournaments/${id}`,
  TOURNAMENT_CREATE: '/tournaments/create',
  TOURNAMENT_EDIT: (id: string | number) => `/tournaments/${id}/edit`,

  // Match routes
  MATCHES: '/matches',
  MATCH_DETAILS: (id: string | number) => `/matches/${id}`,
  MATCH_CREATE: '/matches/create',

  // Player routes
  PLAYERS: '/players',
  PLAYER_DETAILS: (id: string | number) => `/players/${id}`,
  PLAYER_CREATE: '/players/create',

  // User routes
  PROFILE: '/profile',
  SETTINGS: '/settings',

  NOT_FOUND: '/:pathMatch(.*)*',
} as const

export const ROUTE_NAMES = {
  HOME: 'home',
  LOGIN: 'login',
  SIGNUP: 'signup',
  FORGOT_PASSWORD: 'forgot-password',
  RESET_PASSWORD: 'reset-password',
  DASHBOARD: 'dashboard',
  TOURNAMENTS: 'tournaments',
  TOURNAMENT_DETAILS: 'tournament-details',
  TOURNAMENT_CREATE: 'tournament-create',
  TOURNAMENT_EDIT: 'tournament-edit',
  MATCHES: 'matches',
  MATCH_DETAILS: 'match-details',
  PLAYERS: 'players',
  PLAYER_DETAILS: 'player-details',
  PLAYER_CREATE: 'player-create',
  PROFILE: 'profile',
  SETTINGS: 'settings',
  NOT_FOUND: 'notFounds',
} as const

export type RoutePath = (typeof ROUTES)[keyof typeof ROUTES]
export type RouteName = (typeof ROUTE_NAMES)[keyof typeof ROUTE_NAMES]
