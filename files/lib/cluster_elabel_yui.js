function ELabel(A,E,F,C,D,B){this.point=A;this.html=E;this.classname=F||"";this.pixelOffset=C||new GSize(0,0);if(D){if(D<0){D=0}if(D>100){D=100}}this.percentOpacity=D;this.overlap=B||false;this.hidden=false}ELabel.prototype=new GOverlay();ELabel.prototype.initialize=function(A){var C=document.createElement("div");C.style.position="absolute";C.innerHTML='<div class="'+this.classname+'">'+this.html+"</div>";A.getPane(G_MAP_FLOAT_SHADOW_PANE).appendChild(C);this.map_=A;this.div_=C;if(this.percentOpacity){if(typeof (C.style.filter)=="string"){C.style.filter="alpha(opacity:"+this.percentOpacity+")"}if(typeof (C.style.KHTMLOpacity)=="string"){C.style.KHTMLOpacity=this.percentOpacity/100}if(typeof (C.style.MozOpacity)=="string"){C.style.MozOpacity=this.percentOpacity/100}if(typeof (C.style.opacity)=="string"){C.style.opacity=this.percentOpacity/100}}if(this.overlap){var B=GOverlay.getZIndex(this.point.lat());this.div_.style.zIndex=B}if(this.hidden){this.hide()}};ELabel.prototype.remove=function(){this.div_.parentNode.removeChild(this.div_)};ELabel.prototype.copy=function(){return new ELabel(this.point,this.html,this.classname,this.pixelOffset,this.percentOpacity,this.overlap)};ELabel.prototype.redraw=function(B){var C=this.map_.fromLatLngToDivPixel(this.point);var A=parseInt(this.div_.clientHeight);this.div_.style.left=(C.x+this.pixelOffset.width)+"px";this.div_.style.top=(C.y+this.pixelOffset.height-A)+"px"};ELabel.prototype.show=function(){if(this.div_){this.div_.style.display="";this.redraw()}this.hidden=false};ELabel.prototype.hide=function(){if(this.div_){this.div_.style.display="none"}this.hidden=true};ELabel.prototype.isHidden=function(){return this.hidden};ELabel.prototype.supportsHide=function(){return true};ELabel.prototype.setContents=function(A){this.html=A;this.div_.innerHTML='<div class="'+this.classname+'">'+this.html+"</div>";this.redraw(true)};ELabel.prototype.setPoint=function(A){this.point=A;if(this.overlap){var B=GOverlay.getZIndex(this.point.lat());this.div_.style.zIndex=B}this.redraw(true)};ELabel.prototype.setOpacity=function(A){if(A){if(A<0){A=0}if(A>100){A=100}}this.percentOpacity=A;if(this.percentOpacity){if(typeof (this.div_.style.filter)=="string"){this.div_.style.filter="alpha(opacity:"+this.percentOpacity+")"}if(typeof (this.div_.style.KHTMLOpacity)=="string"){this.div_.style.KHTMLOpacity=this.percentOpacity/100}if(typeof (this.div_.style.MozOpacity)=="string"){this.div_.style.MozOpacity=this.percentOpacity/100}if(typeof (this.div_.style.opacity)=="string"){this.div_.style.opacity=this.percentOpacity/100}}};ELabel.prototype.getPoint=function(){return this.point};ELabel.prototype.U=function(){return this.point};ELabel.prototype.V=function(){return this.point};ELabel.prototype.W=function(){return this.point};ELabel.prototype.X=function(){return this.point};ELabel.prototype.Y=function(){return this.point};ELabel.prototype.Z=function(){return this.point};



function ClusterMarker(B,A){this._map=B;this._mapMarkers=[];this._iconBounds=[];this._clusterMarkers=[];this._eventListeners=[];if(typeof (A)==="undefined"){A={}}this.borderPadding=(A.borderPadding)?A.borderPadding:256;this.clusteringEnabled=(A.clusteringEnabled===false)?false:true;if(A.clusterMarkerClick){this.clusterMarkerClick=A.clusterMarkerClick}if(A.clusterMarkerIcon){this.clusterMarkerIcon=A.clusterMarkerIcon}else{this.clusterMarkerIcon=new GIcon();this.clusterMarkerIcon.image="http://maps.google.com/mapfiles/arrow.png";this.clusterMarkerIcon.iconSize=new GSize(39,34);this.clusterMarkerIcon.iconAnchor=new GPoint(9,31);this.clusterMarkerIcon.infoWindowAnchor=new GPoint(9,31);this.clusterMarkerIcon.shadow="http://www.google.com/intl/en_us/mapfiles/arrowshadow.png";this.clusterMarkerIcon.shadowSize=new GSize(39,34)}this.clusterMarkerTitle=(A.clusterMarkerTitle)?A.clusterMarkerTitle:"Click to zoom in and see %count markers";if(A.fitMapMaxZoom){this.fitMapMaxZoom=A.fitMapMaxZoom}this.intersectPadding=(A.intersectPadding)?A.intersectPadding:0;if(A.markers){this.addMarkers(A.markers)}GEvent.bind(this._map,"moveend",this,this._moveEnd);GEvent.bind(this._map,"zoomend",this,this._zoomEnd);GEvent.bind(this._map,"maptypechanged",this,this._mapTypeChanged)}ClusterMarker.prototype.addMarkers=function(B){var A;if(!B[0]){var C=[];for(A in B){C.push(B[A])}B=C}for(A=B.length-1;A>=0;A--){B[A]._isVisible=false;B[A]._isActive=false;B[A]._makeVisible=false}this._mapMarkers=this._mapMarkers.concat(B)};ClusterMarker.prototype._clusterMarker=function(A){function B(K,I,J){return new GMarker(K,{icon:I,title:J})}var F=new GLatLngBounds(),D,H,E=[],C,G=this;for(D=A.length-1;D>=0;D--){C=this._mapMarkers[A[D]];C.index=A[D];F.extend(C.getLatLng());E.push(C)}H=B(F.getCenter(),this.clusterMarkerIcon,this.clusterMarkerTitle.replace(/%count/gi,A.length));H.clusterGroupBounds=F;this._eventListeners.push(GEvent.addListener(H,"click",function(){G.clusterMarkerClick({clusterMarker:H,clusteredMarkers:E})}));return H};ClusterMarker.prototype.clusterMarkerClick=function(A){this._map.setCenter(A.clusterMarker.getLatLng(),this._map.getBoundsZoomLevel(A.clusterMarker.clusterGroupBounds))};ClusterMarker.prototype._filterActiveMapMarkers=function(){var H=this.borderPadding,G=this._map.getZoom(),N=this._map.getCurrentMapType().getProjection(),L,B,J,F,K,C,A=this._map.getBounds(),E,M,D=[],I;if(H){L=N.fromLatLngToPixel(A.getSouthWest(),G);B=new GPoint(L.x-H,L.y+H);J=N.fromPixelToLatLng(B,G);F=N.fromLatLngToPixel(A.getNorthEast(),G);K=new GPoint(F.x+H,F.y-H);C=N.fromPixelToLatLng(K,G);A.extend(J);A.extend(C)}this._activeMarkersChanged=false;if(typeof (this._iconBounds[G])==="undefined"){this._iconBounds[G]=[];this._activeMarkersChanged=true;for(E=this._mapMarkers.length-1;E>=0;E--){M=this._mapMarkers[E];M._isActive=A.containsLatLng(M.getLatLng())?true:false;M._makeVisible=M._isActive;if(M._isActive){D.push(E)}}}else{for(E=this._mapMarkers.length-1;E>=0;E--){M=this._mapMarkers[E];I=M._isActive;M._isActive=A.containsLatLng(M.getLatLng())?true:false;M._makeVisible=M._isActive;if(!this._activeMarkersChanged&&I!==M._isActive){this._activeMarkersChanged=true}if(M._isActive&&typeof (this._iconBounds[G][E])==="undefined"){D.push(E)}}}return D};ClusterMarker.prototype._filterIntersectingMapMarkers=function(){var D,C,B,A=this._map.getZoom();for(C=this._mapMarkers.length-1;C>0;C--){if(this._mapMarkers[C]._makeVisible){D=[];for(B=C-1;B>=0;B--){if(this._mapMarkers[B]._makeVisible&&this._iconBounds[A][C].intersects(this._iconBounds[A][B])){D.push(B)}}if(D.length!==0){D.push(C);for(B=D.length-1;B>=0;B--){this._mapMarkers[D[B]]._makeVisible=false}this._clusterMarkers.push(this._clusterMarker(D))}}}};ClusterMarker.prototype.fitMapToMarkers=function(){var C=this._mapMarkers,D=new GLatLngBounds(),B;for(B=C.length-1;B>=0;B--){D.extend(C[B].getLatLng())}var A=this._map.getBoundsZoomLevel(D);if(this.fitMapMaxZoom&&A>this.fitMapMaxZoom){A=this.fitMapMaxZoom}this._map.setCenter(D.getCenter(),A);this.refresh()};ClusterMarker.prototype._mapTypeChanged=function(){this.refresh(true)};ClusterMarker.prototype._moveEnd=function(){if(!this._cancelMoveEnd){this.refresh()}else{this._cancelMoveEnd=false}};ClusterMarker.prototype._preCacheIconBounds=function(B){var L=this._map.getCurrentMapType().getProjection(),G=this._map.getZoom(),F,M,D,A,H,J,E,I,C,K=this.intersectPadding;for(F=B.length-1;F>=0;F--){M=this._mapMarkers[B[F]];D=M.getIcon().iconSize;A=L.fromLatLngToPixel(M.getLatLng(),G);H=M.getIcon().iconAnchor;J=new GPoint(A.x-H.x-K,A.y-H.y+D.height+K);E=new GPoint(A.x-H.x+D.width+K,A.y-H.y-K);I=L.fromPixelToLatLng(J,G);C=L.fromPixelToLatLng(E,G);this._iconBounds[G][B[F]]=new GLatLngBounds(I,C)}};ClusterMarker.prototype.refresh=function(D){var C,B,A=this._filterActiveMapMarkers();if(this._activeMarkersChanged||D){this._removeClusterMarkers();if(this.clusteringEnabled&&this._map.getZoom()<this._map.getCurrentMapType().getMaximumResolution()){if(A.length>0){this._preCacheIconBounds(A)}this._filterIntersectingMapMarkers()}for(C=this._clusterMarkers.length-1;C>=0;C--){this._map.addOverlay(this._clusterMarkers[C])}for(C=this._mapMarkers.length-1;C>=0;C--){B=this._mapMarkers[C];if(!B._isVisible&&B._makeVisible){this._map.addOverlay(B);B._isVisible=true}if(B._isVisible&&!B._makeVisible){this._map.removeOverlay(B);B._isVisible=false}}}};ClusterMarker.prototype._removeClusterMarkers=function(){for(var A=this._clusterMarkers.length-1;A>=0;A--){this._map.removeOverlay(this._clusterMarkers[A])}for(A=this._eventListeners.length-1;A>=0;A--){GEvent.removeListener(this._eventListeners[A])}this._clusterMarkers=[];this._eventListeners=[]};ClusterMarker.prototype.removeMarkers=function(){for(var A=this._mapMarkers.length-1;A>=0;A--){if(this._mapMarkers[A]._isVisible){this._map.removeOverlay(this._mapMarkers[A])}delete this._mapMarkers[A]._isVisible;delete this._mapMarkers[A]._isActive;delete this._mapMarkers[A]._makeVisible}this._removeClusterMarkers();this._mapMarkers=[];this._iconBounds=[]};ClusterMarker.prototype.triggerClick=function(A){var B=this._mapMarkers[A];if(B._isVisible){GEvent.trigger(B,"click")}else{if(B._isActive){this._map.setCenter(B.getLatLng());this._map.zoomIn();this.triggerClick(A)}else{this._map.setCenter(B.getLatLng());this.triggerClick(A)}}};ClusterMarker.prototype._zoomEnd=function(){this._cancelMoveEnd=true;this.refresh(true)};ClusterMarker.prototype.getVisibleMapMarkers=function(){var A=[];for(i=this._mapMarkers.length-1;i>=0;i--){$marker=this._mapMarkers[i];if($marker._isVisible){A.push(i)}}return A};ClusterMarker.prototype.getActiveMapMarkers=function(){var A=[];for(i=this._mapMarkers.length-1;i>=0;i--){$marker=this._mapMarkers[i];if($marker._isActive){A.push(i)}}return A};