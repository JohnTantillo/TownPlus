class ParkingSpot( var ID: (Int, Int) ) {

  var filled = false

  def checkFilled(): Unit = {
    val response = scala.io.Source.fromURL("http://178.128.238.139/scala").mkString
    println(response)
    if( response == "true" )
      filled = true
    else
      filled = false

  }
}
