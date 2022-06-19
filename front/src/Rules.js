import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';
import TextField from '@mui/material/TextField';
import { Container, Grid } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function Rules(){
    return (
      <div>
        <Box sx = {{height:100}}></Box>
         <Box sx={{ bgcolor: '#ffffff', width: 900,  borderRadius: '16px'}}>
         <Container maxWidth="sm" >
         <Box sx = {{height:50}}></Box>
      <h2>利用規約</h2>
      <Box sx = {{height:20}}></Box>
        <p>
        ユーザーは、本アプリおよび本サービスの利用にあたり、次の各号に定める行為を行うことを禁止します。<br/><br/>

        （１）本アプリを本サービスの利用目的以外の目的で使用すること。<br/>

        （２）本アプリの複製、分解、追加、付加、編集、消去、削除、改変、改造およびその他方法、態様のいかんを問わず本アプリを変更すること。<br/>

        （３）本アプリに関して、リバースエンジニアリング、逆コンバイル、逆アセンブルおよびその他方法、態様のいかんを問わず、本アプリの解析を行うこと。<br/>

        （４）本アプリについて、有償無償を問わず、譲渡、担保設定およびその他の処分、使用許諾等を行うこと。<br/>

        （５）本アプリの著作権表示、所有権を表す標章等を消去、削除およびその他方法、態様のいかんを問わず変更すること、弊社または第三者の名誉、信用、プライバシー、著作権、肖像権、財産権、その他一切の権利を侵害する行為。
        <br/>
        （６）本サービスを違法な目的で不当に利用すること。<br/>

        （７）本サービスに関して、意図的にコンピューターのソフトウェア、ハードウェア、通信機器の機能を妨害、破壊、制限するようにデザインされたコンピューターウィルス、コンピューターコード、ファイル、プログラムを書き込む行為、誤情報や有害なコンピュータープログラム等を送信すること。
        <br/>
        （８）本サービスおよびその他弊社の事業運営に支障をきたす恐れのある行為を行うこと。<br/>

        （９）広告、宣伝その他一切の営業行為および勧誘行為。<br/>

        （１０）社会通念の許容範囲を超えるわいせつな表現、残虐な表現、その他第三者に不快感を与える表現を伴う行為。<br/>

        （１１）他人になりすます行為、未成年者を害する行為、犯罪行為に結びつく行為、ストーキング行為、その他一切の第三者に対する嫌がらせ行為、法令、本規約または公序良俗に反する行為、弊社または第三者の信用を毀損する行為、および弊社または第三者に対し不当に不利益を与えること。
        <br/>
        （１２）その他、弊社が合理的な理由に基づき不適切と判断した一切の行為。<br/><br/>
        本サイトを利用した結果生じたあらゆる損害について、本サイト運営者は一切責任を負いません。
        </p>
        </Container>
        <Box sx = {{height:50}}></Box>
        </Box>
        <Box sx = {{height:100}}></Box>
        </div>
    );
  }
  