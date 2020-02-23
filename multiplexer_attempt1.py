import misc_tools
import random

def create_routing(env, first_step='op1'):

	tasks={
		'op1': {
			'location': env['assembly_bench'],
			'worker': env['assembler'],
			'manned': manned,
			'setup_time': 0.21,
			'run_time': 3.79,
			'teardown_time': 0.14,
			'transit_time': 0.012,
			'route_to': 'op2'
		},

		'op2': misc_tools.make_quality_step(
			env=env,
			run_time=0.2,
			route_to='op3',
			transit_time=0
			),
		'op3': {
			'location': env['machine'],
			'worker': env['technician'],
			'manned': True,
			'setup_time': 0.09,
			'run)time': 1.24,
			'teardown_time': 0.07,
			'transit_time': 0,
			'yeild': 0.99,
			'route_to_pass': env['multiplexer_attempt_kanban'],
			#'route_to_fail': 'rework'
		}
		#'rework': {
		#	'location': env['assembly_bench'],
		#	'worker': env['']
			# I just want to make this pause the entire system when
			# something needs to be debugged... is that reasonable?	
		#}
	}

	return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

	return misc_tools.make_kanban_attrs(order_gen=env['gener.multiplexer_attempt'],
		order_point=2, order_qty=5,
		init_qty=5, warmup_time=0)
	
