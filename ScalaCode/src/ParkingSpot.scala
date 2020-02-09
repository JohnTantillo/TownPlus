class ParkingSpot( var ID: (Int, Int) ) {

  var filled = false

  def checkFilled(): Unit = {
    val response = scala.io.Source.fromURL("http://165.227.223.64/scala").mkString
    if( response == "true" )
      filled = true
    else
      filled = false

    println(filled)
  }
}
