import type { AtomicState, Automata } from '@myshell-ai/ProConfig/types';

const home_page = {
    type: 'state',
    transitions: {
        need_help: 'help_page',
        create_scenario: 'new_scenario'
    }
} satisfies AtomicState;

const new_scenario = {
    type: 'state',
    transitions: {
        ALWAYS: 'scenario_intro'
    }
} satisfies AtomicState;

const scenario_intro = {
    type: 'state',
    transitions: {
        start_chat: 'chat_page',
        create_scenario: 'new_scenario'
    }
} satisfies AtomicState;

const chat_page = {
    type: 'state',
    transitions: {
        CHAT: 'chat_page',
        create_scenario: 'new_scenario'
    }
} satisfies AtomicState;

const help_page = {
    type: 'state',
    transitions: {
        return: 'home_page'
    }
} satisfies AtomicState;

const pepe_talk = {
    id: 'pepe_talk',
    initial: 'home_page',
    states: {
        home_page,
        new_scenario,
        scenario_intro,
        chat_page,
        help_page
    }
} satisfies Automata;
