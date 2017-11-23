class Publisher
  def self.publish
    client = MQTT::Client.new
    client.host = 'amazon-host'
    client.ssl = true
    client.port = 8883
    client.cert_file = Rails.root.join('lib', 'cert', 'rpi.cert.pem').to_s
    client.key_file  = Rails.root.join('lib', 'cert', 'rpi.private.key').to_s
    client.ca_file   = Rails.root.join('lib', 'cert', 'root-CA.crt').to_s
    client.connect do |c|
      hsh = { a: 'aaa', b: 1 }
      msg = hsh.to_json
      c.publish('test', msg)
    end
  end

end
