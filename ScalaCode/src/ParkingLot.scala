import scala.collection.mutable.ArrayBuffer
import scalaj.http._
import play.api.libs.json.JsValue
import play.api.libs.json.Json

class ParkingLot( var rows: Int, var columns: Int ) {

  val lot: Array[Array[String]] = Array.ofDim[String](rows, columns)
  val spots: ArrayBuffer[ParkingSpot] = new ArrayBuffer[ParkingSpot]()
  val total: Int = rows * columns
  var filledSpots: Int = 0
  for( i <- 0 until rows; j <- 0 until columns ) {
    lot(i)(j) = " "
    spots.addOne( new ParkingSpot( (i,j) ) )
  }

  def update(): Unit = {
    filledSpots = 0
    for(spot <- spots){
      spot.checkFilled()
      if(spot.filled){
        lot(spot.ID._1)(spot.ID._2) = "*"
        filledSpots += 1
      }
      else
        lot(spot.ID._1)(spot.ID._2) = " "
    }
//    val blob: JsValue = Json.toJson(lot)
//    val other: String = Json.stringify(blob)
//    Http("http://foo.com/add").postForm.param("data", other).asString
  }

  def percentFilled(): Double = {
    ( filledSpots.asInstanceOf[Double] / total.asInstanceOf[Double] ) * 100
  }

  def filledString(): String = {
    filledSpots + " out of " + total + " spots are currently filled."
  }

  override def toString(): String = {
    var str: String = ""
    for( row <- lot ){
      str += "["
      for( spot <- row ){
        str += " " + spot + ","
      }
      str += "]\n"
    }
    str
  }

}
