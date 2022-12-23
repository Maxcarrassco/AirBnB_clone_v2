# Sets up your web servers for the deployment of web_static

$dirs=['/data/web_static/shared/', '/data/web_static/releases/test/']

exec {'apt-get-update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
}

service {'nginx':
  ensure  =>  'running',
  require => file_line['alias']
}

file {$dir:
ensure  => 'directory',
user    => 'ubuntu',
owner   => 'ubuntu'
}

file {'/data/web_static/releases/test/index.html':
ensure  => 'present',
content => 'Holberton School'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true
}

file_line { 'alias':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => 'location /hbnb_static/ { alias /data/web_static/current/; autoindex off; } location / { ',
  match   => '^\s+location+',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
